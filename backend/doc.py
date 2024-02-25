import os
import sys
import ast
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

model_name = 'SEBIS/code_trans_t5_small_code_documentation_generation_python'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

class CodeVisitor(ast.NodeVisitor):
    # Parses code for functions and class methods
    def __init__(self):
        self.classes = []
        self.functions = []

    def visit_ClassDef(self, node):
        self.classes.append(node)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        if not isinstance(node.parent, ast.ClassDef):
            self.functions.append(node)
        self.generic_visit(node)

def assign_parents(node, parent=None):
    for child in ast.iter_child_nodes(node):
        child.parent = parent
        assign_parents(child, node)

def read_functions(node):
    return ast.unparse(node)

def generate_documentation(code):
    # Runs the model on input code
    inputs = tokenizer(code, return_tensors="pt", max_length=512, truncation=True, padding="max_length")
    summary_ids = model.generate(inputs['input_ids'], max_length=300, length_penalty=2.0, early_stopping=True)
    documentation = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return documentation


def walk_dir(directory):
    # Recursive function that walks through directories and files of root dir
    for root, other_dirs, files in os.walk(directory):
        yield f'{root}', "", "Dir"   

        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    yield f'{file}', f.read(), "File"
        for dir in other_dirs:
            walk_dir(dir)
            

def write_textobj(c, textobject, line, space, x=40,y_offset=750, bottom_margin=50):
    # Writes to the pdf text object
    if (textobject.getY() < bottom_margin):
        c.drawText(textobject)
        c.showPage()
        textobject = c.beginText(x,y_offset)
        textobject.setFont("Times-Roman",12)
    i = 0
    while (i < len(line)):
        length = min(len(line) - i , 90)
        textobject.textLine(f"{space}{line[i:i+length]}")
        i += length
    return textobject
    

def main(main_directory_path, output, process_func=True, process_method=True):
    # Set up the PDF file for output
    c = canvas.Canvas(output, pagesize=letter)
    textobject = c.beginText(40, 750)
    textobject.setFont("Times-Roman", 12)
    for name, code, doc_type in walk_dir(main_directory_path):
        if doc_type == "File":
            textobject.setFont("Times-Bold", 12)
            textobject=write_textobj(c, textobject, f'File: {name}', "    ")
            textobject.setFont("Times-Roman", 12)
            textobject=write_textobj(c, textobject,'Documentation:', "    ")

            documentation = generate_documentation(code)

            for line in documentation.split('\n'):
                textobject=write_textobj(c, textobject, line, "    ")
            
            if (process_func):
                # Generate documentation of the functions
                tree = ast.parse(code)
                visitor = CodeVisitor()
                assign_parents(tree)
                visitor.visit(tree)

                for func in visitor.functions:
                    func_code = read_functions(func)
                    documentation = generate_documentation(func_code)
                    textobject.setFont("Times-Bold", 12)
                    textobject=write_textobj(c, textobject, f'• Function: {func.name}', "        ")
                    textobject.setFont("Times-Roman", 12)
                    textobject=write_textobj(c, textobject, 'Documentation:', "           ")

                    for line in documentation.split('\n'):
                        textobject=write_textobj(c, textobject, line, "               ")


            # Document classes and their methods
            for cls in visitor.classes:
                cls_code = read_functions(cls)
                documentation = generate_documentation(cls_code)
                textobject.setFont("Times-Bold", 12)
                textobject=write_textobj(c, textobject, f'Class: {cls.name}', "    ")
                textobject.setFont("Times-Roman", 12)
                textobject=write_textobj(c, textobject, f"Documentation:", "           ")

                for line in documentation.split('\n'):
                    textobject=write_textobj(c, textobject, line, "               ")

                if process_method:
                    for method in [n for n in cls.body if isinstance(n, ast.FunctionDef)]:
                        method_code = read_functions(method)
                        documentation = generate_documentation(method_code)
                        textobject.setFont("Times-Bold", 12)
                        textobject=write_textobj(c, textobject, f"• Method: {method.name}", "        ")
                        textobject.setFont("Times-Roman", 12)
                        textobject=write_textobj(c, textobject, f'Documentation: {line}', "               ")

                        for line in documentation.split('\n'):
                            textobject=write_textobj(c, textobject, line, "               ")
                textobject.textLine('')
            textobject.textLine('')
        else:
            textobject=write_textobj(c, textobject, "------------------------------------","")
            textobject.setFont("Times-Roman", 18)
            textobject=write_textobj(c, textobject, f"Directory: {name}", "")
            textobject.setFont("Times-Roman", 12)

    # Finalize the PDF
    c.drawText(textobject)
    c.showPage()
    c.save()

if len(sys.argv) != 3:
        print("Usage: python doc.py <INPUT_DIRECTORY> <OUTPUT_DIRECTORY>")
        sys.exit(1)

input_directory = sys.argv[1]
output_pdf = sys.argv[2]

# Validate input directory
if not os.path.isdir(input_directory):
    print(f"The specified input directory does not exist: {input_directory}")
    sys.exit(1)

main(input_directory, output_pdf)
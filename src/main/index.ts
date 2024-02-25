import { app, shell, dialog, BrowserWindow, ipcMain, ipcRenderer } from 'electron'
import { join } from 'path'
import { electronApp, optimizer, is } from '@electron-toolkit/utils'
import icon from '../../resources/icon.png?asset'
import { spawn } from 'child_process'
import fs from 'fs'

function createWindow(): void {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    show: false,
    useContentSize: true,
    autoHideMenuBar: true,
    resizable: false,
    backgroundColor: '6e679b',

    ...(process.platform === 'linux' ? { icon } : {}),
    webPreferences: {
      nodeIntegration: true,
      preload: join(__dirname, '../preload/index.js'),
      sandbox: false
    }
  })

  mainWindow.on('ready-to-show', () => {
    mainWindow.show()
  })

  mainWindow.webContents.setWindowOpenHandler((details) => {
    shell.openExternal(details.url)
    return { action: 'deny' }
  })

  // HMR for renderer base on electron-vite cli.
  // Load the remote URL for development or the local html file for production.
  if (is.dev && process.env['ELECTRON_RENDERER_URL']) {
    mainWindow.loadURL(process.env['ELECTRON_RENDERER_URL'])
  } else {
    mainWindow.loadFile(join(__dirname, '../renderer/index.html'))
  }
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
  // Set app user model id for windows
  electronApp.setAppUserModelId('com.electron')

  // Default open or close DevTools by F12 in development
  // and ignore CommandOrControl + R in production.
  // see https://github.com/alex8088/electron-toolkit/tree/master/packages/utils
  app.on('browser-window-created', (_, window) => {
    optimizer.watchWindowShortcuts(window)
  })

  createWindow()
  
  ipcMain.on('file_open', (event, type) => {
    dialog.showOpenDialog({ properties: ['openDirectory'] }).then((path) => {
      console.log(path.filePaths[0]);
      event.sender.send('file_path', type, path.filePaths[0]);
    })
  })
  
  ipcMain.on('generate', (event, input_dir, output_dir, functions, methods) => {
    console.log("Generation called!");
    console.log(input_dir);
    console.log(output_dir + "/docs.pdf");
    console.log(functions);
    console.log(methods);
    console.log(join(__dirname, '../../backend/doc.py'));
    const python = spawn('python', [join(__dirname, '..', '..','backend','doc.py'), input_dir, join(output_dir,"docs.pdf"), functions, methods]);
    python.stdout.on('data', data => console.log('data : ', data.toString()))
    python.on('close', ()=>{
      console.log("Generation complete!");
      event.sender.send('completion');
    })
  })
  
  app.on('activate', function () {
    // On macOS it's common to re-create a window in the app when the
    // dock icon is clicked and there are no other windows open.
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

// In this file you can include the rest of your app"s specific main process
// code. You can also put them in separate files and require them here.

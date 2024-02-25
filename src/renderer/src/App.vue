<script setup lang="ts">
import Versions from './components/Versions.vue'

const ipcHandle = () => window.electron.ipcRenderer.send('ping')
</script>

<template>
  <div class="frame">
    <div class="overlap-wrapper">
      <div class="overlap">
        <div class="overlap-group">
          <div class="text-wrapper">Select Directories</div>
          <div class="div">Additional Options</div>
          <div class="additional-options">
            <div class="methods">
              <div class="overlap-group-2">
                <div class="text-wrapper-2">Methods</div>
                <input class="addition-options-checkbox" type="checkbox" id="methods" v-model="methods_checked" />
              </div>
            </div>
            <div class="functions">
              <div class="overlap-group-2">
                <div class="text-wrapper-2">Functions</div>
                <input class="addition-options-checkbox" type="checkbox" id="functions" v-model="functions_checked" />
              </div>
            </div>
          </div>
          <div class="output">
            <div class="overlap-group-wrapper">
              <div class="div-wrapper">
                <div class="text-wrapper-3">Select Output</div>
              </div>
            </div>
            <div class="div-wrapper-2">
              <div class="div-wrapper-3">
                <input class="form" v-model="output_dir_path">
              </div>
            </div>
          </div>
          <div class="input">
            <div class="overlap-group-wrapper">
              <div class="div-wrapper">
                <div class="text-wrapper-5">Select Input</div>
              </div>
            </div>
            <div class="div-wrapper-2">
              <div class="div-wrapper-3">
                <input class="form" v-model="input_dir_path">
              </div>
            </div>
          </div>
        </div>
        <div class="overlap-2">
          <div class="text-wrapper-6">DocPDFGen</div>
        </div>
        <div class="generate">
          <div class="overlap-group-3">
            <button class="text-wrapper-7" @click="test">GENERATE</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "Frame",
  data() {
    return {
      input_dir_path: "",
      output_dir_path: "",
      methods_checked: null,
      functions_checked: null,
    }
  },
  methods: {
    test(event) {
      alert("Test called");
      this.methods_checked === true;
      this.functions_checked === true;
      console.log(this.input_dir_path);
      console.log(this.output_dir_path);
    }
  }
});

</script>

<style>
.frame {
  background-color: #6e679b;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}

.frame .overlap-wrapper {
  background-color: #6e679b;
  height: 474px;
  width: 551px;
}

.frame .overlap {
  background-color: #6e679b;
  height: 47px;
  position: relative;
}

.frame .overlap-group {
  background-color: #9584ab;
  border-radius: 8px;
  height: 296px;
  left: 66px;
  position: absolute;
  top: 89px;
  width: 425px;
}

.frame .text-wrapper {
  color: #ffffff;
  font-family: "Inter-Regular", Helvetica;
  font-size: 24px;
  font-weight: 400;
  left: 112px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  top: 14px;
}

.frame .div {
  color: #ffffff;
  font-family: "Inter-Regular", Helvetica;
  font-size: 24px;
  font-weight: 400;
  left: 110px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  top: 184px;
}

.frame .additional-options {
  height: 36px;
  left: 24px;
  position: absolute;
  top: 228px;
  width: 371px;
}

.frame .methods {
  height: 36px;
  left: 199px;
  position: absolute;
  top: 0;
  width: 174px;
}

.frame .overlap-group-2 {
  background-color: #7d608b;
  border-radius: 25px;
  height: 36px;
  position: relative;
  width: 172px;
}

.frame .text-wrapper-2 {
  color: #ffffff;
  font-family: "Inter-ExtraBold", Helvetica;
  font-size: 16px;
  font-weight: 800;
  height: 31px;
  left: 67px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  text-align: center;
  top: 2px;
  width: 8px;
}

.frame .rectangle {
  background-color: #d9d9d9;
  border: 3px solid;
  border-color: #653974;
  border-radius: 22px;
  height: 22px;
  left: 13px;
  position: absolute;
  top: 3px;
  width: 22px;
}

.frame .functions {
  height: 36px;
  left: 0;
  position: absolute;
  top: 0;
  width: 174px;
}

.frame .output {
  height: 48px;
  left: 14px;
  position: absolute;
  top: 112px;
  width: 397px;
}

.frame .overlap-group-wrapper {
  height: 47px;
  left: 0;
  position: absolute;
  top: 1px;
  width: 174px;
}

.frame .div-wrapper {
  background-color: #653974;
  border-radius: 38px;
  height: 47px;
  position: relative;
  width: 172px;
}

.frame .text-wrapper-3 {
  color: #ebc2ff;
  font-family: "Inter-Bold", Helvetica;
  font-size: 15px;
  font-weight: 700;
  height: 30px;
  left: 29px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  text-align: center;
  top: 9px;
  width: 115px;
}

.frame .div-wrapper-2 {
  align-items: flex-start;
  display: flex;
  flex-direction: column;
  gap: 8px;
  height: 48px;
  left: 195px;
  position: absolute;
  top: 0;
  width: 202px;
}

.frame .div-wrapper-3 {
  align-items: center;
  align-self: stretch;
  background-color: #ffffff;
  border: 2px solid;
  border-color: #d9d9d9;
  border-radius: 8px;
  display: flex;
  flex: 0 0 auto;
  gap: 8px;
  overflow: hidden;
  padding: 12px 16px;
  position: relative;
  width: 80;
}

.frame .text-wrapper-4 {
  color: #000000;
  flex: 1;
  font-family: "Inter-Italic", Helvetica;
  font-size: 15px;
  font-style: italic;
  font-weight: 400;
  letter-spacing: 0;
  line-height: 24px;
  margin-top: -2px;
  opacity: 0.5;
  position: relative;
}

.frame .input {
  height: 48px;
  left: 14px;
  position: absolute;
  top: 55px;
  width: 397px;
}

.frame .text-wrapper-5 {
  color: #ebc2ff;
  font-family: "Inter-Bold", Helvetica;
  font-size: 15px;
  font-weight: 700;
  height: 23px;
  left: 32px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  text-align: center;
  top: 12px;
  width: 109px;
}

.frame .overlap-2 {
  background-color: #3f2462;
  border-radius: 8px;
  height: 57px;
  left: 66px;
  position: absolute;
  top: 20px;
  width: 425px;
}

.frame .text-wrapper-6 {
  color: #f6eaf8;
  font-family: "Inter-ExtraBold", Helvetica;
  font-size: 40px;
  font-weight: 800;
  left: 94px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  top: 3px;
  white-space: nowrap;
}

.frame .generate {
  height: 47px;
  left: 66px;
  position: absolute;
  top: 402px;
  width: 427px;
}

.frame .overlap-group-3 {
  background-color: #d9d9d9;
  border-radius: 38px;
  height: 47px;
  position: relative;
  width: 425px;
}

.frame .text-wrapper-7 {
  color: #581677;
  font-family: "Inter-Bold", Helvetica;
  font-size: 20px;
  font-weight: 700;
  height: 23px;
  left: 130px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  text-align: center;
  top: 12px;
  white-space: nowrap;
  width: 158px;
}

.app-container {
  background-color: #6e679b;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

html, body {
  background-color: #6e679b;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.addition-options-checkbox {
  margin-left: 5;
  margin: 2;
  padding: 0;
  width: 50%;
  height: 50%;
}

.form {
  width: 40;
  size: 5;
}
</style>
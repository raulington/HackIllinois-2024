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
                <div class="rectangle" />
              </div>
            </div>
            <div class="functions">
              <div class="overlap-group-2">
                <div class="text-wrapper-2">Functions</div>
                <div class="rectangle">
                <input type="checkbox" id="checkbox" v-model="checked" />
<label for="checkbox">{{ checked }}</label>
                </div>
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
                <div class="text-wrapper-4">Output Directory Path</div>
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
                <input type="text" id="myTextField" name="myTextField">
              </div>
            </div>
          </div>
        </div>
        <div class="overlap-2">
          <div class="text-wrapper-6">DocPDFGen</div>
        </div>
        <div class="generate">
          <div class="overlap-group-3">
            <div class="text-wrapper-7">GENERATE</div>
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
  background-color: #ffffff;
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
  width: 83px;
}

.frame .rectangle {
  background-color: #d9d9d9;
  border: 3px solid;
  border-color: #653974;
  border-radius: 22px;
  height: 22px;
  left: 15px;
  position: absolute;
  top: 7px;
  width: 26px;
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
  width: 100%;
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
  overflow: hidden;
}
</style>
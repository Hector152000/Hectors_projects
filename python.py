import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy.io import wavfile # Audio data reading
import sounddevice as sd
from IPython.display import Audio
st.set_option('deprecation.showPyplotGlobalUse', False)



audio_file = open('/home/cherot/Escritorio/CORONAVIRUS.wav', 'rb')
audio_coronavirus = audio_file.read()
audio_file = open('/home/cherot/Escritorio/Hola.wav', 'rb')
audio_hola = audio_file.read()

f_hl, dt_hl = wavfile.read('/home/cherot/Escritorio/Hola.wav')
f_cv, dt_cv= wavfile.read('/home/cherot/Escritorio/CORONAVIRUS.wav')


st.title('VOICE ANALYZER 5000')
st.write('Esta app sirve para distinguir dos palabras: **HOLA** y **CORONAVIRUS** \n ___\n Empezamos por **Hola**')
a=len(dt_hl)/f_hl
t=np.arange(0,a,1/f_hl)

plt.plot(t,dt_hl, linewidth='0.8')
st.pyplot(fig=None)
st.audio(audio_hola, format='audio/wav')

st.write('___ \n Ahora  **CORONAVIRUS**')
a=len(dt_cv)/f_hl
t=np.arange(0,a,1/f_cv)

plt.plot(t,dt_cv, linewidth='0.8', label='AUDIO CORONAVIRUS')
st.pyplot(fig=None)
st.audio(audio_coronavirus, format='audio/wav')
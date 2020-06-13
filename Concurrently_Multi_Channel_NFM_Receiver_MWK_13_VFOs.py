#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: MWK_Multi_Channels_NFM_Scanner_13_VFOs
# Author: MWK
# Description: MWK Multi Channels Scanner 13 VFOs
# GNU Radio version: 3.7.13.5
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class Concurrently_Multi_Channel_NFM_Receiver_MWK_13_VFOs(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="MWK_Multi_Channels_NFM_Scanner_13_VFOs")

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 100
        self.sql_lev = sql_lev = -50
        self.samp_rate = samp_rate = 1e6
        self.rfgain = rfgain = 15
        self.ppm_correction = ppm_correction = 15
        self.down_rate = down_rate = 250e3
        self.channel_width = channel_width = 250e3
        self.channel_freq_9 = channel_freq_9 = 424.033e6
        self.channel_freq_8 = channel_freq_8 = 424.786e6
        self.channel_freq_7 = channel_freq_7 = 424.900e6
        self.channel_freq_6 = channel_freq_6 = 424.580e6
        self.channel_freq_5 = channel_freq_5 = 424.9875e6
        self.channel_freq_4 = channel_freq_4 = 424.1875e6
        self.channel_freq_3 = channel_freq_3 = 424.700e6
        self.channel_freq_13 = channel_freq_13 = 424.786e6
        self.channel_freq_12 = channel_freq_12 = 424.588e6
        self.channel_freq_11 = channel_freq_11 = 425.175e6
        self.channel_freq_10 = channel_freq_10 = 424.3875e6
        self.channel_freq2 = channel_freq2 = 424.2875e6
        self.channel_freq1 = channel_freq1 = 424.4875e6
        self.center_freq = center_freq = 424.5e6

        ##################################################
        # Blocks
        ##################################################
        _volume_sizer = wx.BoxSizer(wx.VERTICAL)
        self._volume_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	label='Vol.',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._volume_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_volume_sizer,
        	value=self.volume,
        	callback=self.set_volume,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_volume_sizer, 0, 16, 1, 1)
        _sql_lev_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sql_lev_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_sql_lev_sizer,
        	value=self.sql_lev,
        	callback=self.set_sql_lev,
        	label='SQL',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._sql_lev_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_sql_lev_sizer,
        	value=self.sql_lev,
        	callback=self.set_sql_lev,
        	minimum=-100,
        	maximum=100,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_sql_lev_sizer, 1, 16, 1, 4)
        _rfgain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._rfgain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_rfgain_sizer,
        	value=self.rfgain,
        	callback=self.set_rfgain,
        	label='RF Gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._rfgain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_rfgain_sizer,
        	value=self.rfgain,
        	callback=self.set_rfgain,
        	minimum=0,
        	maximum=48,
        	num_steps=12,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_rfgain_sizer, 1, 0, 1, 4)
        _ppm_correction_sizer = wx.BoxSizer(wx.VERTICAL)
        self._ppm_correction_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_ppm_correction_sizer,
        	value=self.ppm_correction,
        	callback=self.set_ppm_correction,
        	label='PPM Corr.',
        	converter=forms.int_converter(),
        	proportion=0,
        )
        self._ppm_correction_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_ppm_correction_sizer,
        	value=self.ppm_correction,
        	callback=self.set_ppm_correction,
        	minimum=-60,
        	maximum=60,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=int,
        	proportion=1,
        )
        self.Add(_ppm_correction_sizer)
        _channel_freq_9_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq_9_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq_9_sizer,
        	value=self.channel_freq_9,
        	callback=self.set_channel_freq_9,
        	label='VFO-9',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq_9_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq_9_sizer,
        	value=self.channel_freq_9,
        	callback=self.set_channel_freq_9,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_channel_freq_9_sizer, 3, 0, 1, 4)
        _channel_freq_8_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq_8_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq_8_sizer,
        	value=self.channel_freq_8,
        	callback=self.set_channel_freq_8,
        	label='VFO-3',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq_8_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq_8_sizer,
        	value=self.channel_freq_8,
        	callback=self.set_channel_freq_8,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_channel_freq_8_sizer, 1, 12, 1, 4)
        _channel_freq_7_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq_7_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq_7_sizer,
        	value=self.channel_freq_7,
        	callback=self.set_channel_freq_7,
        	label='VFO-4',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq_7_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq_7_sizer,
        	value=self.channel_freq_7,
        	callback=self.set_channel_freq_7,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_channel_freq_7_sizer, 2, 0, 1, 4)
        _channel_freq_6_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq_6_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq_6_sizer,
        	value=self.channel_freq_6,
        	callback=self.set_channel_freq_6,
        	label='VFO-7',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq_6_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq_6_sizer,
        	value=self.channel_freq_6,
        	callback=self.set_channel_freq_6,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_channel_freq_6_sizer, 2, 12, 1, 4)
        _channel_freq_5_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq_5_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq_5_sizer,
        	value=self.channel_freq_5,
        	callback=self.set_channel_freq_5,
        	label='VFO-6',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq_5_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq_5_sizer,
        	value=self.channel_freq_5,
        	callback=self.set_channel_freq_5,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_channel_freq_5_sizer, 2, 8, 1, 4)
        _channel_freq_4_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq_4_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq_4_sizer,
        	value=self.channel_freq_4,
        	callback=self.set_channel_freq_4,
        	label='VFO-5',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq_4_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq_4_sizer,
        	value=self.channel_freq_4,
        	callback=self.set_channel_freq_4,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_channel_freq_4_sizer, 2, 4, 1, 4)
        _channel_freq_3_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq_3_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq_3_sizer,
        	value=self.channel_freq_3,
        	callback=self.set_channel_freq_3,
        	label='VFO-2',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq_3_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq_3_sizer,
        	value=self.channel_freq_3,
        	callback=self.set_channel_freq_3,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_channel_freq_3_sizer, 1, 8, 1, 4)
        _channel_freq_13_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq_13_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq_13_sizer,
        	value=self.channel_freq_13,
        	callback=self.set_channel_freq_13,
        	label='VFO-13',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq_13_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq_13_sizer,
        	value=self.channel_freq_13,
        	callback=self.set_channel_freq_13,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_channel_freq_13_sizer, 3, 16, 1, 4)
        _channel_freq_12_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq_12_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq_12_sizer,
        	value=self.channel_freq_12,
        	callback=self.set_channel_freq_12,
        	label='VFO-12',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq_12_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq_12_sizer,
        	value=self.channel_freq_12,
        	callback=self.set_channel_freq_12,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_channel_freq_12_sizer, 3, 12, 1, 4)
        _channel_freq_11_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq_11_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq_11_sizer,
        	value=self.channel_freq_11,
        	callback=self.set_channel_freq_11,
        	label='VFO-11',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq_11_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq_11_sizer,
        	value=self.channel_freq_11,
        	callback=self.set_channel_freq_11,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_channel_freq_11_sizer, 3, 8, 1, 4)
        _channel_freq_10_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq_10_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq_10_sizer,
        	value=self.channel_freq_10,
        	callback=self.set_channel_freq_10,
        	label='VFO-10',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq_10_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq_10_sizer,
        	value=self.channel_freq_10,
        	callback=self.set_channel_freq_10,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_channel_freq_10_sizer, 3, 4, 1, 4)
        _channel_freq2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq2_sizer,
        	value=self.channel_freq2,
        	callback=self.set_channel_freq2,
        	label='VFO-1',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq2_sizer,
        	value=self.channel_freq2,
        	callback=self.set_channel_freq2,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_channel_freq2_sizer, 1, 4, 1, 4)
        _channel_freq1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._channel_freq1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_channel_freq1_sizer,
        	value=self.channel_freq1,
        	callback=self.set_channel_freq1,
        	label='VFO-8',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._channel_freq1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_channel_freq1_sizer,
        	value=self.channel_freq1,
        	callback=self.set_channel_freq1,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_channel_freq1_sizer, 2, 16, 1, 4)
        _center_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._center_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_center_freq_sizer,
        	value=self.center_freq,
        	callback=self.set_center_freq,
        	label='Center Freq.',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._center_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_center_freq_sizer,
        	value=self.center_freq,
        	callback=self.set_center_freq,
        	minimum=400e6,
        	maximum=470e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_center_freq_sizer)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=center_freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=None,
        	title='MWK Concurrently Multi Channels NFM 13 VFOs Memory Scanner',
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.rational_resampler_xxx_0_1_2_1_4 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_1_2_1_3 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_1_2_1_2 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_1_2_1_1 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_1_2_1_0 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_1_2_1 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_1_2_0 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_1_2 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_1_1 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_1_0 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_1 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=24,
                decimation=250,
                taps=None,
                fractional_bw=None,
        )
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq, 0)
        self.osmosdr_source_0.set_freq_corr(ppm_correction, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(rfgain, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.low_pass_filter_0_1_2_1_4 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 0.5e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2_1_3 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2_1_2 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2_1_1 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2_1_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2_1 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_1 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(int(samp_rate/channel_width), firdes.low_pass(
        	1, samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_2_1_4 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_2_1_3 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_2_1_2 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_2_1_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_2_1_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_2_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_2_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_2 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_xx_0_1_2_1_4 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1_2_1_3 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1_2_1_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1_2_1_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1_2_1_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1_2_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1_2_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1_2 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0_1_2_1_4 = blocks.multiply_const_vff((volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2_1_3 = blocks.multiply_const_vff((volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2_1_2 = blocks.multiply_const_vff((volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2_1_1 = blocks.multiply_const_vff((volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2_1_0 = blocks.multiply_const_vff((volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2_1 = blocks.multiply_const_vff((volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2_0 = blocks.multiply_const_vff((volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2 = blocks.multiply_const_vff((volume/100, ))
        self.blocks_multiply_const_vxx_0_1_1 = blocks.multiply_const_vff((volume/100, ))
        self.blocks_multiply_const_vxx_0_1_0 = blocks.multiply_const_vff((volume/100, ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vff((volume/100, ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((volume/100, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume/100, ))
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_sink_0 = audio.sink(24000, '', True)
        self.analog_simple_squelch_cc_2_4 = analog.simple_squelch_cc(-50, 1e-4)
        self.analog_simple_squelch_cc_2_3 = analog.simple_squelch_cc(-50, 1e-4)
        self.analog_simple_squelch_cc_2_2 = analog.simple_squelch_cc(-50, 1e-4)
        self.analog_simple_squelch_cc_2_1 = analog.simple_squelch_cc(-50, 1e-4)
        self.analog_simple_squelch_cc_2_0 = analog.simple_squelch_cc(-50, 1e-4)
        self.analog_simple_squelch_cc_2 = analog.simple_squelch_cc(-50, 1e-4)
        self.analog_simple_squelch_cc_1 = analog.simple_squelch_cc(-50, 1e-4)
        self.analog_simple_squelch_cc_0_0_2_0 = analog.simple_squelch_cc(-50, 1e-4)
        self.analog_simple_squelch_cc_0_0_2 = analog.simple_squelch_cc(-50, 1e-4)
        self.analog_simple_squelch_cc_0_0_1 = analog.simple_squelch_cc(-50, 1e-4)
        self.analog_simple_squelch_cc_0_0_0 = analog.simple_squelch_cc(-50, 1e-4)
        self.analog_simple_squelch_cc_0_0 = analog.simple_squelch_cc(-50, 1e-4)
        self.analog_simple_squelch_cc_0 = analog.simple_squelch_cc(-50, 1e-4)
        self.analog_sig_source_x_0_1_2_1_4 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq_8, 1, 0)
        self.analog_sig_source_x_0_1_2_1_3 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq_13, 1, 0)
        self.analog_sig_source_x_0_1_2_1_2 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq_12, 1, 0)
        self.analog_sig_source_x_0_1_2_1_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq_11, 1, 0)
        self.analog_sig_source_x_0_1_2_1_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq_10, 1, 0)
        self.analog_sig_source_x_0_1_2_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq_9, 1, 0)
        self.analog_sig_source_x_0_1_2_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq_7, 1, 0)
        self.analog_sig_source_x_0_1_2 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq_6, 1, 0)
        self.analog_sig_source_x_0_1_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq_5, 1, 0)
        self.analog_sig_source_x_0_1_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq_4, 1, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq_3, 1, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq2, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq - channel_freq1, 1, 0)
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_ff(sql_lev, 1, 1, True)
        self.analog_fm_demod_cf_1 = analog.fm_demod_cf(
        	channel_rate=down_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=1.0,
        	tau=75e-6,
        )
        self.analog_fm_demod_cf_0_0_2_1_4 = analog.fm_demod_cf(
        	channel_rate=down_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=1.0,
        	tau=75e-6,
        )
        self.analog_fm_demod_cf_0_0_2_1_3 = analog.fm_demod_cf(
        	channel_rate=down_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=1.0,
        	tau=75e-6,
        )
        self.analog_fm_demod_cf_0_0_2_1_2 = analog.fm_demod_cf(
        	channel_rate=down_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=1.0,
        	tau=75e-6,
        )
        self.analog_fm_demod_cf_0_0_2_1_1 = analog.fm_demod_cf(
        	channel_rate=down_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=1.0,
        	tau=75e-6,
        )
        self.analog_fm_demod_cf_0_0_2_1_0 = analog.fm_demod_cf(
        	channel_rate=down_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=1.0,
        	tau=75e-6,
        )
        self.analog_fm_demod_cf_0_0_2_1 = analog.fm_demod_cf(
        	channel_rate=down_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=1.0,
        	tau=75e-6,
        )
        self.analog_fm_demod_cf_0_0_2_0 = analog.fm_demod_cf(
        	channel_rate=down_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=1.0,
        	tau=75e-6,
        )
        self.analog_fm_demod_cf_0_0_2 = analog.fm_demod_cf(
        	channel_rate=down_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=1.0,
        	tau=75e-6,
        )
        self.analog_fm_demod_cf_0_0_1 = analog.fm_demod_cf(
        	channel_rate=down_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=1.0,
        	tau=75e-6,
        )
        self.analog_fm_demod_cf_0_0_0 = analog.fm_demod_cf(
        	channel_rate=down_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=1.0,
        	tau=75e-6,
        )
        self.analog_fm_demod_cf_0_0 = analog.fm_demod_cf(
        	channel_rate=down_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=1.0,
        	tau=75e-6,
        )
        self.analog_fm_demod_cf_0 = analog.fm_demod_cf(
        	channel_rate=down_rate,
        	audio_decim=1,
        	deviation=75000,
        	audio_pass=15000,
        	audio_stop=16000,
        	gain=1.0,
        	tau=75e-6,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fm_demod_cf_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.analog_fm_demod_cf_0_0, 0), (self.rational_resampler_xxx_0_1, 0))
        self.connect((self.analog_fm_demod_cf_0_0_0, 0), (self.rational_resampler_xxx_0_1_0, 0))
        self.connect((self.analog_fm_demod_cf_0_0_1, 0), (self.rational_resampler_xxx_0_1_1, 0))
        self.connect((self.analog_fm_demod_cf_0_0_2, 0), (self.rational_resampler_xxx_0_1_2, 0))
        self.connect((self.analog_fm_demod_cf_0_0_2_0, 0), (self.rational_resampler_xxx_0_1_2_0, 0))
        self.connect((self.analog_fm_demod_cf_0_0_2_1, 0), (self.rational_resampler_xxx_0_1_2_1, 0))
        self.connect((self.analog_fm_demod_cf_0_0_2_1_0, 0), (self.rational_resampler_xxx_0_1_2_1_0, 0))
        self.connect((self.analog_fm_demod_cf_0_0_2_1_1, 0), (self.rational_resampler_xxx_0_1_2_1_1, 0))
        self.connect((self.analog_fm_demod_cf_0_0_2_1_2, 0), (self.rational_resampler_xxx_0_1_2_1_2, 0))
        self.connect((self.analog_fm_demod_cf_0_0_2_1_3, 0), (self.rational_resampler_xxx_0_1_2_1_3, 0))
        self.connect((self.analog_fm_demod_cf_0_0_2_1_4, 0), (self.rational_resampler_xxx_0_1_2_1_4, 0))
        self.connect((self.analog_fm_demod_cf_1, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.analog_sig_source_x_0_1_0, 0), (self.blocks_multiply_xx_0_1_0, 1))
        self.connect((self.analog_sig_source_x_0_1_1, 0), (self.blocks_multiply_xx_0_1_1, 1))
        self.connect((self.analog_sig_source_x_0_1_2, 0), (self.blocks_multiply_xx_0_1_2, 1))
        self.connect((self.analog_sig_source_x_0_1_2_0, 0), (self.blocks_multiply_xx_0_1_2_0, 1))
        self.connect((self.analog_sig_source_x_0_1_2_1, 0), (self.blocks_multiply_xx_0_1_2_1, 1))
        self.connect((self.analog_sig_source_x_0_1_2_1_0, 0), (self.blocks_multiply_xx_0_1_2_1_0, 1))
        self.connect((self.analog_sig_source_x_0_1_2_1_1, 0), (self.blocks_multiply_xx_0_1_2_1_1, 1))
        self.connect((self.analog_sig_source_x_0_1_2_1_2, 0), (self.blocks_multiply_xx_0_1_2_1_2, 1))
        self.connect((self.analog_sig_source_x_0_1_2_1_3, 0), (self.blocks_multiply_xx_0_1_2_1_3, 1))
        self.connect((self.analog_sig_source_x_0_1_2_1_4, 0), (self.blocks_multiply_xx_0_1_2_1_4, 1))
        self.connect((self.analog_simple_squelch_cc_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_simple_squelch_cc_0_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.analog_simple_squelch_cc_0_0_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.analog_simple_squelch_cc_0_0_1, 0), (self.blocks_throttle_0_0_1, 0))
        self.connect((self.analog_simple_squelch_cc_0_0_2, 0), (self.blocks_throttle_0_0_2, 0))
        self.connect((self.analog_simple_squelch_cc_0_0_2_0, 0), (self.blocks_throttle_0_0_2_0, 0))
        self.connect((self.analog_simple_squelch_cc_1, 0), (self.blocks_throttle_1, 0))
        self.connect((self.analog_simple_squelch_cc_2, 0), (self.blocks_throttle_0_0_2_1, 0))
        self.connect((self.analog_simple_squelch_cc_2_0, 0), (self.blocks_throttle_0_0_2_1_0, 0))
        self.connect((self.analog_simple_squelch_cc_2_1, 0), (self.blocks_throttle_0_0_2_1_1, 0))
        self.connect((self.analog_simple_squelch_cc_2_2, 0), (self.blocks_throttle_0_0_2_1_2, 0))
        self.connect((self.analog_simple_squelch_cc_2_3, 0), (self.blocks_throttle_0_0_2_1_3, 0))
        self.connect((self.analog_simple_squelch_cc_2_4, 0), (self.blocks_throttle_0_0_2_1_4, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.analog_pwr_squelch_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_multiply_const_vxx_0_1_0, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_multiply_const_vxx_0_1_1, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_multiply_const_vxx_0_1_2, 0), (self.blocks_add_xx_0, 5))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_0, 0), (self.blocks_add_xx_0, 6))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_1, 0), (self.blocks_add_xx_0, 7))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_1_0, 0), (self.blocks_add_xx_0, 9))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_1_1, 0), (self.blocks_add_xx_0, 10))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_1_2, 0), (self.blocks_add_xx_0, 11))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_1_3, 0), (self.blocks_add_xx_0, 12))
        self.connect((self.blocks_multiply_const_vxx_0_1_2_1_4, 0), (self.blocks_add_xx_0, 8))
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.low_pass_filter_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.low_pass_filter_0_1, 0))
        self.connect((self.blocks_multiply_xx_0_1_0, 0), (self.low_pass_filter_0_1_0, 0))
        self.connect((self.blocks_multiply_xx_0_1_1, 0), (self.low_pass_filter_0_1_1, 0))
        self.connect((self.blocks_multiply_xx_0_1_2, 0), (self.low_pass_filter_0_1_2, 0))
        self.connect((self.blocks_multiply_xx_0_1_2_0, 0), (self.low_pass_filter_0_1_2_0, 0))
        self.connect((self.blocks_multiply_xx_0_1_2_1, 0), (self.low_pass_filter_0_1_2_1, 0))
        self.connect((self.blocks_multiply_xx_0_1_2_1_0, 0), (self.low_pass_filter_0_1_2_1_0, 0))
        self.connect((self.blocks_multiply_xx_0_1_2_1_1, 0), (self.low_pass_filter_0_1_2_1_1, 0))
        self.connect((self.blocks_multiply_xx_0_1_2_1_2, 0), (self.low_pass_filter_0_1_2_1_2, 0))
        self.connect((self.blocks_multiply_xx_0_1_2_1_3, 0), (self.low_pass_filter_0_1_2_1_3, 0))
        self.connect((self.blocks_multiply_xx_0_1_2_1_4, 0), (self.low_pass_filter_0_1_2_1_4, 0))
        self.connect((self.blocks_throttle_0, 0), (self.analog_fm_demod_cf_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.analog_fm_demod_cf_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.analog_fm_demod_cf_0_0_0, 0))
        self.connect((self.blocks_throttle_0_0_1, 0), (self.analog_fm_demod_cf_0_0_1, 0))
        self.connect((self.blocks_throttle_0_0_2, 0), (self.analog_fm_demod_cf_0_0_2, 0))
        self.connect((self.blocks_throttle_0_0_2_0, 0), (self.analog_fm_demod_cf_0_0_2_0, 0))
        self.connect((self.blocks_throttle_0_0_2_1, 0), (self.analog_fm_demod_cf_0_0_2_1, 0))
        self.connect((self.blocks_throttle_0_0_2_1_0, 0), (self.analog_fm_demod_cf_0_0_2_1_0, 0))
        self.connect((self.blocks_throttle_0_0_2_1_1, 0), (self.analog_fm_demod_cf_0_0_2_1_1, 0))
        self.connect((self.blocks_throttle_0_0_2_1_2, 0), (self.analog_fm_demod_cf_0_0_2_1_2, 0))
        self.connect((self.blocks_throttle_0_0_2_1_3, 0), (self.analog_fm_demod_cf_0_0_2_1_3, 0))
        self.connect((self.blocks_throttle_0_0_2_1_4, 0), (self.analog_fm_demod_cf_0_0_2_1_4, 0))
        self.connect((self.blocks_throttle_1, 0), (self.analog_fm_demod_cf_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_simple_squelch_cc_0, 0))
        self.connect((self.low_pass_filter_0_0, 0), (self.analog_simple_squelch_cc_1, 0))
        self.connect((self.low_pass_filter_0_1, 0), (self.analog_simple_squelch_cc_0_0, 0))
        self.connect((self.low_pass_filter_0_1_0, 0), (self.analog_simple_squelch_cc_0_0_0, 0))
        self.connect((self.low_pass_filter_0_1_1, 0), (self.analog_simple_squelch_cc_0_0_1, 0))
        self.connect((self.low_pass_filter_0_1_2, 0), (self.analog_simple_squelch_cc_0_0_2, 0))
        self.connect((self.low_pass_filter_0_1_2_0, 0), (self.analog_simple_squelch_cc_0_0_2_0, 0))
        self.connect((self.low_pass_filter_0_1_2_1, 0), (self.analog_simple_squelch_cc_2, 0))
        self.connect((self.low_pass_filter_0_1_2_1_0, 0), (self.analog_simple_squelch_cc_2_0, 0))
        self.connect((self.low_pass_filter_0_1_2_1_1, 0), (self.analog_simple_squelch_cc_2_1, 0))
        self.connect((self.low_pass_filter_0_1_2_1_2, 0), (self.analog_simple_squelch_cc_2_2, 0))
        self.connect((self.low_pass_filter_0_1_2_1_3, 0), (self.analog_simple_squelch_cc_2_3, 0))
        self.connect((self.low_pass_filter_0_1_2_1_4, 0), (self.analog_simple_squelch_cc_2_4, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_1_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_1_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_1_2, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_1_2_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_1_2_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_1_2_1_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_1_2_1_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_1_2_1_2, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_1_2_1_3, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0_1_2_1_4, 0))
        self.connect((self.osmosdr_source_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_1, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.rational_resampler_xxx_0_1_0, 0), (self.blocks_multiply_const_vxx_0_1_0, 0))
        self.connect((self.rational_resampler_xxx_0_1_1, 0), (self.blocks_multiply_const_vxx_0_1_1, 0))
        self.connect((self.rational_resampler_xxx_0_1_2, 0), (self.blocks_multiply_const_vxx_0_1_2, 0))
        self.connect((self.rational_resampler_xxx_0_1_2_0, 0), (self.blocks_multiply_const_vxx_0_1_2_0, 0))
        self.connect((self.rational_resampler_xxx_0_1_2_1, 0), (self.blocks_multiply_const_vxx_0_1_2_1, 0))
        self.connect((self.rational_resampler_xxx_0_1_2_1_0, 0), (self.blocks_multiply_const_vxx_0_1_2_1_0, 0))
        self.connect((self.rational_resampler_xxx_0_1_2_1_1, 0), (self.blocks_multiply_const_vxx_0_1_2_1_1, 0))
        self.connect((self.rational_resampler_xxx_0_1_2_1_2, 0), (self.blocks_multiply_const_vxx_0_1_2_1_2, 0))
        self.connect((self.rational_resampler_xxx_0_1_2_1_3, 0), (self.blocks_multiply_const_vxx_0_1_2_1_3, 0))
        self.connect((self.rational_resampler_xxx_0_1_2_1_4, 0), (self.blocks_multiply_const_vxx_0_1_2_1_4, 0))

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self._volume_slider.set_value(self.volume)
        self._volume_text_box.set_value(self.volume)
        self.blocks_multiply_const_vxx_0_1_2_1_4.set_k((self.volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2_1_3.set_k((self.volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2_1_2.set_k((self.volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2_1_1.set_k((self.volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2_1_0.set_k((self.volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2_1.set_k((self.volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2_0.set_k((self.volume/100, ))
        self.blocks_multiply_const_vxx_0_1_2.set_k((self.volume/100, ))
        self.blocks_multiply_const_vxx_0_1_1.set_k((self.volume/100, ))
        self.blocks_multiply_const_vxx_0_1_0.set_k((self.volume/100, ))
        self.blocks_multiply_const_vxx_0_1.set_k((self.volume/100, ))
        self.blocks_multiply_const_vxx_0_0.set_k((self.volume/100, ))
        self.blocks_multiply_const_vxx_0.set_k((self.volume/100, ))

    def get_sql_lev(self):
        return self.sql_lev

    def set_sql_lev(self, sql_lev):
        self.sql_lev = sql_lev
        self._sql_lev_slider.set_value(self.sql_lev)
        self._sql_lev_text_box.set_value(self.sql_lev)
        self.analog_pwr_squelch_xx_0.set_threshold(self.sql_lev)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_1_2_1_4.set_taps(firdes.low_pass(1, self.samp_rate, 0.5e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2_1_3.set_taps(firdes.low_pass(1, self.samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2_1_2.set_taps(firdes.low_pass(1, self.samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2_1_1.set_taps(firdes.low_pass(1, self.samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2_1_0.set_taps(firdes.low_pass(1, self.samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2_1.set_taps(firdes.low_pass(1, self.samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2_0.set_taps(firdes.low_pass(1, self.samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_2.set_taps(firdes.low_pass(1, self.samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_1.set_taps(firdes.low_pass(1, self.samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1_0.set_taps(firdes.low_pass(1, self.samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_1.set_taps(firdes.low_pass(1, self.samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 1e3, 12.5e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_2_1_4.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_2_1_3.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_2_1_2.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_2_1_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_2_1_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_2_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_2.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_1.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_1_2_1_4.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_2_1_3.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_2_1_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_2_1_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_2_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_2_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_2_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_rfgain(self):
        return self.rfgain

    def set_rfgain(self, rfgain):
        self.rfgain = rfgain
        self._rfgain_slider.set_value(self.rfgain)
        self._rfgain_text_box.set_value(self.rfgain)
        self.osmosdr_source_0.set_gain(self.rfgain, 0)

    def get_ppm_correction(self):
        return self.ppm_correction

    def set_ppm_correction(self, ppm_correction):
        self.ppm_correction = ppm_correction
        self._ppm_correction_slider.set_value(self.ppm_correction)
        self._ppm_correction_text_box.set_value(self.ppm_correction)
        self.osmosdr_source_0.set_freq_corr(self.ppm_correction, 0)

    def get_down_rate(self):
        return self.down_rate

    def set_down_rate(self, down_rate):
        self.down_rate = down_rate

    def get_channel_width(self):
        return self.channel_width

    def set_channel_width(self, channel_width):
        self.channel_width = channel_width

    def get_channel_freq_9(self):
        return self.channel_freq_9

    def set_channel_freq_9(self, channel_freq_9):
        self.channel_freq_9 = channel_freq_9
        self._channel_freq_9_slider.set_value(self.channel_freq_9)
        self._channel_freq_9_text_box.set_value(self.channel_freq_9)
        self.analog_sig_source_x_0_1_2_1.set_frequency(self.center_freq - self.channel_freq_9)

    def get_channel_freq_8(self):
        return self.channel_freq_8

    def set_channel_freq_8(self, channel_freq_8):
        self.channel_freq_8 = channel_freq_8
        self._channel_freq_8_slider.set_value(self.channel_freq_8)
        self._channel_freq_8_text_box.set_value(self.channel_freq_8)
        self.analog_sig_source_x_0_1_2_1_4.set_frequency(self.center_freq - self.channel_freq_8)

    def get_channel_freq_7(self):
        return self.channel_freq_7

    def set_channel_freq_7(self, channel_freq_7):
        self.channel_freq_7 = channel_freq_7
        self._channel_freq_7_slider.set_value(self.channel_freq_7)
        self._channel_freq_7_text_box.set_value(self.channel_freq_7)
        self.analog_sig_source_x_0_1_2_0.set_frequency(self.center_freq - self.channel_freq_7)

    def get_channel_freq_6(self):
        return self.channel_freq_6

    def set_channel_freq_6(self, channel_freq_6):
        self.channel_freq_6 = channel_freq_6
        self._channel_freq_6_slider.set_value(self.channel_freq_6)
        self._channel_freq_6_text_box.set_value(self.channel_freq_6)
        self.analog_sig_source_x_0_1_2.set_frequency(self.center_freq - self.channel_freq_6)

    def get_channel_freq_5(self):
        return self.channel_freq_5

    def set_channel_freq_5(self, channel_freq_5):
        self.channel_freq_5 = channel_freq_5
        self._channel_freq_5_slider.set_value(self.channel_freq_5)
        self._channel_freq_5_text_box.set_value(self.channel_freq_5)
        self.analog_sig_source_x_0_1_1.set_frequency(self.center_freq - self.channel_freq_5)

    def get_channel_freq_4(self):
        return self.channel_freq_4

    def set_channel_freq_4(self, channel_freq_4):
        self.channel_freq_4 = channel_freq_4
        self._channel_freq_4_slider.set_value(self.channel_freq_4)
        self._channel_freq_4_text_box.set_value(self.channel_freq_4)
        self.analog_sig_source_x_0_1_0.set_frequency(self.center_freq - self.channel_freq_4)

    def get_channel_freq_3(self):
        return self.channel_freq_3

    def set_channel_freq_3(self, channel_freq_3):
        self.channel_freq_3 = channel_freq_3
        self._channel_freq_3_slider.set_value(self.channel_freq_3)
        self._channel_freq_3_text_box.set_value(self.channel_freq_3)
        self.analog_sig_source_x_0_1.set_frequency(self.center_freq - self.channel_freq_3)

    def get_channel_freq_13(self):
        return self.channel_freq_13

    def set_channel_freq_13(self, channel_freq_13):
        self.channel_freq_13 = channel_freq_13
        self._channel_freq_13_slider.set_value(self.channel_freq_13)
        self._channel_freq_13_text_box.set_value(self.channel_freq_13)
        self.analog_sig_source_x_0_1_2_1_3.set_frequency(self.center_freq - self.channel_freq_13)

    def get_channel_freq_12(self):
        return self.channel_freq_12

    def set_channel_freq_12(self, channel_freq_12):
        self.channel_freq_12 = channel_freq_12
        self._channel_freq_12_slider.set_value(self.channel_freq_12)
        self._channel_freq_12_text_box.set_value(self.channel_freq_12)
        self.analog_sig_source_x_0_1_2_1_2.set_frequency(self.center_freq - self.channel_freq_12)

    def get_channel_freq_11(self):
        return self.channel_freq_11

    def set_channel_freq_11(self, channel_freq_11):
        self.channel_freq_11 = channel_freq_11
        self._channel_freq_11_slider.set_value(self.channel_freq_11)
        self._channel_freq_11_text_box.set_value(self.channel_freq_11)
        self.analog_sig_source_x_0_1_2_1_1.set_frequency(self.center_freq - self.channel_freq_11)

    def get_channel_freq_10(self):
        return self.channel_freq_10

    def set_channel_freq_10(self, channel_freq_10):
        self.channel_freq_10 = channel_freq_10
        self._channel_freq_10_slider.set_value(self.channel_freq_10)
        self._channel_freq_10_text_box.set_value(self.channel_freq_10)
        self.analog_sig_source_x_0_1_2_1_0.set_frequency(self.center_freq - self.channel_freq_10)

    def get_channel_freq2(self):
        return self.channel_freq2

    def set_channel_freq2(self, channel_freq2):
        self.channel_freq2 = channel_freq2
        self._channel_freq2_slider.set_value(self.channel_freq2)
        self._channel_freq2_text_box.set_value(self.channel_freq2)
        self.analog_sig_source_x_0_0.set_frequency(self.center_freq - self.channel_freq2)

    def get_channel_freq1(self):
        return self.channel_freq1

    def set_channel_freq1(self, channel_freq1):
        self.channel_freq1 = channel_freq1
        self._channel_freq1_slider.set_value(self.channel_freq1)
        self._channel_freq1_text_box.set_value(self.channel_freq1)
        self.analog_sig_source_x_0.set_frequency(self.center_freq - self.channel_freq1)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self._center_freq_slider.set_value(self.center_freq)
        self._center_freq_text_box.set_value(self.center_freq)
        self.wxgui_fftsink2_0.set_baseband_freq(self.center_freq)
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)
        self.analog_sig_source_x_0_1_2_1_4.set_frequency(self.center_freq - self.channel_freq_8)
        self.analog_sig_source_x_0_1_2_1_3.set_frequency(self.center_freq - self.channel_freq_13)
        self.analog_sig_source_x_0_1_2_1_2.set_frequency(self.center_freq - self.channel_freq_12)
        self.analog_sig_source_x_0_1_2_1_1.set_frequency(self.center_freq - self.channel_freq_11)
        self.analog_sig_source_x_0_1_2_1_0.set_frequency(self.center_freq - self.channel_freq_10)
        self.analog_sig_source_x_0_1_2_1.set_frequency(self.center_freq - self.channel_freq_9)
        self.analog_sig_source_x_0_1_2_0.set_frequency(self.center_freq - self.channel_freq_7)
        self.analog_sig_source_x_0_1_2.set_frequency(self.center_freq - self.channel_freq_6)
        self.analog_sig_source_x_0_1_1.set_frequency(self.center_freq - self.channel_freq_5)
        self.analog_sig_source_x_0_1_0.set_frequency(self.center_freq - self.channel_freq_4)
        self.analog_sig_source_x_0_1.set_frequency(self.center_freq - self.channel_freq_3)
        self.analog_sig_source_x_0_0.set_frequency(self.center_freq - self.channel_freq2)
        self.analog_sig_source_x_0.set_frequency(self.center_freq - self.channel_freq1)


def main(top_block_cls=Concurrently_Multi_Channel_NFM_Receiver_MWK_13_VFOs, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()

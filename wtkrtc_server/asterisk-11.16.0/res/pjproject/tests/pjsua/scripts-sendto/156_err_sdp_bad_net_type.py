# $Id: 156_err_sdp_bad_net_type.py 369517 2012-07-01 17:28:57Z file $
import inc_sip as sip
import inc_sdp as sdp

sdp = \
"""
v=0
o=- 0 0 IN IP4 127.0.0.1
s=pjmedia
c=AF IP4 127.0.0.1
t=0 0
m=audio 4000 RTP/AVP 0 101
a=rtpmap:0 PCMU/8000
a=sendrecv
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
"""

pjsua_args = "--null-audio --auto-answer 200"
extra_headers = ""
include = [ "Warning: " ]	# better have Warning header
exclude = []
sendto_cfg = sip.SendtoCfg("Bad SDP network type", pjsua_args, sdp, 400, 
			   extra_headers=extra_headers,
			   resp_inc=include, resp_exc=exclude) 
			   


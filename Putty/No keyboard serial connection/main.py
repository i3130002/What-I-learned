<!DOCTYPE html>
<!-- saved from url=(0117)file:///D:/D/project/other/WhatILearned/NodeMCU%20ESP8266/Micropython/webrepl-master/webrepl.html#192.168.1.100:8266/ -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=windows-1252"><style id="term-style">.terminal {
  float: left;
  border: #000000 solid 5px;
  font-family: "DejaVu Sans Mono", "Liberation Mono", monospace;
  font-size: 11px;
  color: #f0f0f0;
  background: #000000;
}

.terminal-cursor {
  color: #000000;
  background: #f0f0f0;
}
</style>
<title>MicroPython WebREPL</title>
<!--
  term.js
  Copyright (c) 2012-2013, Christopher Jeffrey (MIT License)
  Copyright (c) 2016, Paul Sokolovsky
-->
<style>
  html {
    background: #555;
  }

  h1 {
    margin-bottom: 20px;
    font: 20px/1.5 sans-serif;
  }

/*
  .terminal {
    float: left;
    border: #000 solid 5px;
    font-family: "DejaVu Sans Mono", "Liberation Mono", monospace;
    font-size: 11px;
    color: #f0f0f0;
    background: #000;
  }

  .terminal-cursor {
    color: #000;
    background: #f0f0f0;
  }
*/

  .file-box {
    margin: 4px;
    padding: 4px;
    background: #888;
  }
</style>
<script src="./main_files/term.js.download"></script>
<script src="./main_files/FileSaver.js.download"></script>
</head>
<body>

<div style="display:inline-block; vertical-align:top;">
<form>
<input type="text" name="webrepl_url" id="url" value="ws://192.168.4.1:8266/">
<input type="submit" id="button" value="Connect" onclick="button_click(); return false;">
</form>
<div id="term">
<div class="terminal" tabindex="0" spellcheck="false" style="outline: none; background-color: rgb(0, 0, 0); color: rgb(240, 240, 240);"><div>pplication/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange</div><div>;v=b3\r\nReferer:&nbsp;http://192.168.1.100/?led=on\r\nAccept-Encoding:&nbsp;gzip,&nbsp;deflate</div><div>\r\nAccept-Language:&nbsp;fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\n'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>LED&nbsp;OFF&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>Got&nbsp;a&nbsp;connection&nbsp;from&nbsp;('192.168.1.101',&nbsp;48283)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>Content&nbsp;=&nbsp;b'GET&nbsp;/?led=on&nbsp;HTTP/1.1\r\nHost:&nbsp;192.168.1.100\r\nConnection:&nbsp;keep-ali</div><div>ve\r\nUpgrade-Insecure-Requests:&nbsp;1\r\nDNT:&nbsp;1\r\nSave-Data:&nbsp;on\r\nUser-Agent:&nbsp;Moz</div><div>illa/5.0&nbsp;(Linux;&nbsp;Android&nbsp;9;&nbsp;MI&nbsp;6X)&nbsp;AppleWebKit/537.36&nbsp;(KHTML,&nbsp;like&nbsp;Gecko)&nbsp;Chrome</div><div>/75.0.3770.89&nbsp;Mobile&nbsp;Safari/537.36\r\nAccept:&nbsp;text/html,application/xhtml+xml,ap</div><div>plication/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;</div><div>v=b3\r\nReferer:&nbsp;http://192.168.1.100/?led=off\r\nAccept-Encoding:&nbsp;gzip,&nbsp;deflate</div><div>\r\nAccept-Language:&nbsp;fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\n'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>LED&nbsp;ON&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>Got&nbsp;a&nbsp;connection&nbsp;from&nbsp;('192.168.1.101',&nbsp;48285)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>Content&nbsp;=&nbsp;b'GET&nbsp;/?led=off&nbsp;HTTP/1.1\r\nHost:&nbsp;192.168.1.100\r\nConnection:&nbsp;keep-al</div><div>ive\r\nUpgrade-Insecure-Requests:&nbsp;1\r\nDNT:&nbsp;1\r\nSave-Data:&nbsp;on\r\nUser-Agent:&nbsp;Mo</div><div>zilla/5.0&nbsp;(Linux;&nbsp;Android&nbsp;9;&nbsp;MI&nbsp;6X)&nbsp;AppleWebKit/537.36&nbsp;(KHTML,&nbsp;like&nbsp;Gecko)&nbsp;Chrom</div><div>e/75.0.3770.89&nbsp;Mobile&nbsp;Safari/537.36\r\nAccept:&nbsp;text/html,application/xhtml+xml,a</div><div>pplication/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange</div><div>;v=b3\r\nReferer:&nbsp;http://192.168.1.100/?led=on\r\nAccept-Encoding:&nbsp;gzip,&nbsp;deflate</div><div>\r\nAccept-Language:&nbsp;fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\n'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>LED&nbsp;OFF&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>Got&nbsp;a&nbsp;connection&nbsp;from&nbsp;('192.168.1.101',&nbsp;48287)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>Content&nbsp;=&nbsp;b'GET&nbsp;/?led=on&nbsp;HTTP/1.1\r\nHost:&nbsp;192.168.1.100\r\nConnection:&nbsp;keep-ali</div><div>ve\r\nUpgrade-Insecure-Requests:&nbsp;1\r\nDNT:&nbsp;1\r\nSave-Data:&nbsp;on\r\nUser-Agent:&nbsp;Moz</div><div>illa/5.0&nbsp;(Linux;&nbsp;Android&nbsp;9;&nbsp;MI&nbsp;6X)&nbsp;AppleWebKit/537.36&nbsp;(KHTML,&nbsp;like&nbsp;Gecko)&nbsp;Chrome</div><div>/75.0.3770.89&nbsp;Mobile&nbsp;Safari/537.36\r\nAccept:&nbsp;text/html,application/xhtml+xml,ap</div><div>plication/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;</div><div>v=b3\r\nReferer:&nbsp;http://192.168.1.100/?led=off\r\nAccept-Encoding:&nbsp;gzip,&nbsp;deflate</div><div>\r\nAccept-Language:&nbsp;fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\n'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>LED&nbsp;ON&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>Got&nbsp;a&nbsp;connection&nbsp;from&nbsp;('192.168.1.101',&nbsp;48289)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>Content&nbsp;=&nbsp;b'GET&nbsp;/?led=off&nbsp;HTTP/1.1\r\nHost:&nbsp;192.168.1.100\r\nConnection:&nbsp;keep-al</div><div>ive\r\nUpgrade-Insecure-Requests:&nbsp;1\r\nDNT:&nbsp;1\r\nSave-Data:&nbsp;on\r\nUser-Agent:&nbsp;Mo</div><div>zilla/5.0&nbsp;(Linux;&nbsp;Android&nbsp;9;&nbsp;MI&nbsp;6X)&nbsp;AppleWebKit/537.36&nbsp;(KHTML,&nbsp;like&nbsp;Gecko)&nbsp;Chrom</div><div>e/75.0.3770.89&nbsp;Mobile&nbsp;Safari/537.36\r\nAccept:&nbsp;text/html,application/xhtml+xml,a</div><div>pplication/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange</div><div>;v=b3\r\nReferer:&nbsp;http://192.168.1.100/?led=on\r\nAccept-Encoding:&nbsp;gzip,&nbsp;deflate</div><div>\r\nAccept-Language:&nbsp;fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\n'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>LED&nbsp;OFF&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>Got&nbsp;a&nbsp;connection&nbsp;from&nbsp;('192.168.1.101',&nbsp;48295)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>Content&nbsp;=&nbsp;b'GET&nbsp;/?led=on&nbsp;HTTP/1.1\r\nHost:&nbsp;192.168.1.100\r\nConnection:&nbsp;keep-ali</div><div>ve\r\nUpgrade-Insecure-Requests:&nbsp;1\r\nDNT:&nbsp;1\r\nSave-Data:&nbsp;on\r\nUser-Agent:&nbsp;Moz</div><div>illa/5.0&nbsp;(Linux;&nbsp;Android&nbsp;9;&nbsp;MI&nbsp;6X)&nbsp;AppleWebKit/537.36&nbsp;(KHTML,&nbsp;like&nbsp;Gecko)&nbsp;Chrome</div><div>/75.0.3770.89&nbsp;Mobile&nbsp;Safari/537.36\r\nAccept:&nbsp;text/html,application/xhtml+xml,ap</div><div>plication/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;</div><div>v=b3\r\nReferer:&nbsp;http://192.168.1.100/?led=off\r\nAccept-Encoding:&nbsp;gzip,&nbsp;deflate</div><div>\r\nAccept-Language:&nbsp;fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7\r\n\r\n'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>LED&nbsp;ON&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>Got&nbsp;a&nbsp;connection&nbsp;from&nbsp;('192.168.1.101',&nbsp;48297)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>Traceback&nbsp;(most&nbsp;recent&nbsp;call&nbsp;last):&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>&nbsp;&nbsp;File&nbsp;"main.py",&nbsp;line&nbsp;35,&nbsp;in&nbsp;&lt;module&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>OSError:&nbsp;[Errno&nbsp;104]&nbsp;ECONNRESET&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>MicroPython&nbsp;v1.11-8-g48dcbbe60&nbsp;on&nbsp;2019-05-29;&nbsp;ESP&nbsp;module&nbsp;with&nbsp;ESP8266&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div>Type&nbsp;"help()"&nbsp;for&nbsp;more&nbsp;information.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div></div></div>
</div>

<div id="file-boxes" style="display:inline-block; vertical-align:top; width:230px;">

  <div class="file-box">
    <strong>Send a file</strong>
    <input type="file" id="put-file-select">
    <div id="put-file-list">main.py - 916977 bytes</div>
    <input type="button" value="Send to device" id="put-file-button" onclick="put_file(); return false;">
  </div>

  <div class="file-box">
    <strong>Get a file</strong>
    <input type="text" name="get_filename" id="get_filename" value="" size="13">
    <input type="button" value="Get from device" onclick="get_file(); return false;">
  </div>

  <div class="file-box" id="file-status">Sent main.py, 916977 bytes</div>

</div>

<br clear="both">
<i>Terminal widget should be focused (text cursor visible) to accept input. Click on it if not.</i><br>
<i>To paste, press Ctrl+A, then Ctrl+V</i>


<script>
;

var term;
var ws;
var connected = false;
var binary_state = 0;
var put_file_name = null;
var put_file_data = null;
var get_file_name = null;
var get_file_data = null;

function calculate_size(win) {
    var cols = Math.max(80, Math.min(150, (win.innerWidth - 280) / 7)) | 0;
    var rows = Math.max(24, Math.min(80, (win.innerHeight - 180) / 12)) | 0;
    return [cols, rows];
}

(function() {
    window.onload = function() {
      var url = window.location.hash.substring(1);
      if (url) {
        document.getElementById('url').value = 'ws://' + url;
      }
      var size = calculate_size(self);
      term = new Terminal({
        cols: size[0],
        rows: size[1],
        useStyle: true,
        screenKeys: true,
        cursorBlink: false
      });
      term.open(document.getElementById("term"));
      show_https_warning();
    };
    window.addEventListener('resize', function() {
        var size = calculate_size(self);
        term.resize(size[0], size[1]);
    });
}).call(this);

function show_https_warning() {
    if (window.location.protocol == 'https:') {
        var warningDiv = document.createElement('div');
        warningDiv.style.cssText = 'background:#f99;padding:5px;margin-bottom:10px;line-height:1.5em;text-align:center';
        warningDiv.innerHTML = [
            'At this time, the WebREPL client cannot be accessed over HTTPS connections.',
            'Use a HTTP connection, eg. <a href="http://micropython.org/webrepl/">http://micropython.org/webrepl/</a>.',
            'Alternatively, download the files from <a href="https://github.com/micropython/webrepl">GitHub</a> and run them locally.'
        ].join('<br>');
        document.body.insertBefore(warningDiv, document.body.childNodes[0]);
        term.resize(term.cols, term.rows - 7);
    }
}

function button_click() {
    if (connected) {
        ws.close();
    } else {
        document.getElementById('url').disabled = true;
        document.getElementById('button').value = "Disconnect";
        connected = true;
        connect(document.getElementById('url').value);
    }
}

function prepare_for_connect() {
    document.getElementById('url').disabled = false;
    document.getElementById('button').value = "Connect";
}

function update_file_status(s) {
    document.getElementById('file-status').innerHTML = s;
}

function connect(url) {
    window.location.hash = url.substring(5);
    ws = new WebSocket(url);
    ws.binaryType = 'arraybuffer';
    ws.onopen = function() {
        term.removeAllListeners('data');
        term.on('data', function(data) {
            // Pasted data from clipboard will likely contain
            // LF as EOL chars.
            data = data.replace(/\n/g, "\r");
            ws.send(data);
        });

        term.on('title', function(title) {
            document.title = title;
        });

        term.focus();
        term.element.focus();
        term.write('\x1b[31mWelcome to MicroPython!\x1b[m\r\n');

        ws.onmessage = function(event) {
            if (event.data instanceof ArrayBuffer) {
                var data = new Uint8Array(event.data);
                switch (binary_state) {
                    case 11:
                        // first response for put
                        if (decode_resp(data) == 0) {
                            // send file data in chunks
                            for (var offset = 0; offset < put_file_data.length; offset += 1024) {
                                ws.send(put_file_data.slice(offset, offset + 1024));
                            }
                            binary_state = 12;
                        }
                        break;
                    case 12:
                        // final response for put
                        if (decode_resp(data) == 0) {
                            update_file_status('Sent ' + put_file_name + ', ' + put_file_data.length + ' bytes');
                        } else {
                            update_file_status('Failed sending ' + put_file_name);
                        }
                        binary_state = 0;
                        break;

                    case 21:
                        // first response for get
                        if (decode_resp(data) == 0) {
                            binary_state = 22;
                            var rec = new Uint8Array(1);
                            rec[0] = 0;
                            ws.send(rec);
                        }
                        break;
                    case 22: {
                        // file data
                        var sz = data[0] | (data[1] << 8);
                        if (data.length == 2 + sz) {
                            // we assume that the data comes in single chunks
                            if (sz == 0) {
                                // end of file
                                binary_state = 23;
                            } else {
                                // accumulate incoming data to get_file_data
                                var new_buf = new Uint8Array(get_file_data.length + sz);
                                new_buf.set(get_file_data);
                                new_buf.set(data.slice(2), get_file_data.length);
                                get_file_data = new_buf;
                                update_file_status('Getting ' + get_file_name + ', ' + get_file_data.length + ' bytes');

                                var rec = new Uint8Array(1);
                                rec[0] = 0;
                                ws.send(rec);
                            }
                        } else {
                            binary_state = 0;
                        }
                        break;
                    }
                    case 23:
                        // final response
                        if (decode_resp(data) == 0) {
                            update_file_status('Got ' + get_file_name + ', ' + get_file_data.length + ' bytes');
                            saveAs(new Blob([get_file_data], {type: "application/octet-stream"}), get_file_name);
                        } else {
                            update_file_status('Failed getting ' + get_file_name);
                        }
                        binary_state = 0;
                        break;
                    case 31:
                        // first (and last) response for GET_VER
                        console.log('GET_VER', data);
                        binary_state = 0;
                        break;
                }
            }
            term.write(event.data);
        };
    };

    ws.onclose = function() {
        connected = false;
        if (term) {
            term.write('\x1b[31mDisconnected\x1b[m\r\n');
        }
        term.off('data');
        prepare_for_connect();
    }
}

function decode_resp(data) {
    if (data[0] == 'W'.charCodeAt(0) && data[1] == 'B'.charCodeAt(0)) {
        var code = data[2] | (data[3] << 8);
        return code;
    } else {
        return -1;
    }
}

function put_file() {
    var dest_fname = put_file_name;
    var dest_fsize = put_file_data.length;

    // WEBREPL_FILE = "<2sBBQLH64s"
    var rec = new Uint8Array(2 + 1 + 1 + 8 + 4 + 2 + 64);
    rec[0] = 'W'.charCodeAt(0);
    rec[1] = 'A'.charCodeAt(0);
    rec[2] = 1; // put
    rec[3] = 0;
    rec[4] = 0; rec[5] = 0; rec[6] = 0; rec[7] = 0; rec[8] = 0; rec[9] = 0; rec[10] = 0; rec[11] = 0;
    rec[12] = dest_fsize & 0xff; rec[13] = (dest_fsize >> 8) & 0xff; rec[14] = (dest_fsize >> 16) & 0xff; rec[15] = (dest_fsize >> 24) & 0xff;
    rec[16] = dest_fname.length & 0xff; rec[17] = (dest_fname.length >> 8) & 0xff;
    for (var i = 0; i < 64; ++i) {
        if (i < dest_fname.length) {
            rec[18 + i] = dest_fname.charCodeAt(i);
        } else {
            rec[18 + i] = 0;
        }
    }

    // initiate put
    binary_state = 11;
    update_file_status('Sending ' + put_file_name + '...');
    ws.send(rec);
}

function get_file() {
    var src_fname = document.getElementById('get_filename').value;

    // WEBREPL_FILE = "<2sBBQLH64s"
    var rec = new Uint8Array(2 + 1 + 1 + 8 + 4 + 2 + 64);
    rec[0] = 'W'.charCodeAt(0);
    rec[1] = 'A'.charCodeAt(0);
    rec[2] = 2; // get
    rec[3] = 0;
    rec[4] = 0; rec[5] = 0; rec[6] = 0; rec[7] = 0; rec[8] = 0; rec[9] = 0; rec[10] = 0; rec[11] = 0;
    rec[12] = 0; rec[13] = 0; rec[14] = 0; rec[15] = 0;
    rec[16] = src_fname.length & 0xff; rec[17] = (src_fname.length >> 8) & 0xff;
    for (var i = 0; i < 64; ++i) {
        if (i < src_fname.length) {
            rec[18 + i] = src_fname.charCodeAt(i);
        } else {
            rec[18 + i] = 0;
        }
    }

    // initiate get
    binary_state = 21;
    get_file_name = src_fname;
    get_file_data = new Uint8Array(0);
    update_file_status('Getting ' + get_file_name + '...');
    ws.send(rec);
}

function get_ver() {
    // WEBREPL_REQ_S = "<2sBBQLH64s"
    var rec = new Uint8Array(2 + 1 + 1 + 8 + 4 + 2 + 64);
    rec[0] = 'W'.charCodeAt(0);
    rec[1] = 'A'.charCodeAt(0);
    rec[2] = 3; // GET_VER
    // rest of "rec" is zero

    // initiate GET_VER
    binary_state = 31;
    ws.send(rec);
}

function handle_put_file_select(evt) {
    // The event holds a FileList object which is a list of File objects,
    // but we only support single file selection at the moment.
    var files = evt.target.files;

    // Get the file info and load its data.
    var f = files[0];
    put_file_name = f.name;
    var reader = new FileReader();
    reader.onload = function(e) {
        put_file_data = new Uint8Array(e.target.result);
        document.getElementById('put-file-list').innerHTML = '' + escape(put_file_name) + ' - ' + put_file_data.length + ' bytes';
        document.getElementById('put-file-button').disabled = false;
    };
    reader.readAsArrayBuffer(f);
}

document.getElementById('put-file-select').addEventListener('click', function(){
    this.value = null;
}, false);

document.getElementById('put-file-select').addEventListener('change', handle_put_file_select, false);
document.getElementById('put-file-button').disabled = true;

</script>


</body></html>
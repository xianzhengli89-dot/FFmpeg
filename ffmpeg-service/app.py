from flask import Flask, request, jsonify
import subprocess
import os
import urllib.request
import tempfile

app = Flask(__name__)

@app.route('/')
def home():
    return "🎬 FFmpeg视频处理服务运行正常！<br><a href='/test'>测试FFmpeg</a>"

@app.route('/overlay', methods=['POST'])
def video_overlay():
    try:
        data = request.json
        
        # 获取参数
        background_url = data.get('background_url')
        overlay_url = data.get('overlay_url')
        output_filename = data.get('output_filename', 'output.mp4')
        
        return {
            "status": "success",
            "message": "✅ 成功收到视频处理请求！",
            "data_received": {
                "background": background_url,
                "overlay": overlay_url,
                "output": output_filename
            }
        }
                
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'处理错误: {str(e)}'
        }), 500

@app.route('/test')
def test():
    try:
        result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
        return f"<h3>FFmpeg测试结果：</h3><pre>{result.stdout}</pre>"
    except Exception as e:
        return f"<h3>FFmpeg测试失败：</h3><pre>{str(e)}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
#!/bin/bash
./mediamtx &
ffmpeg -input_format yuyv422 -f v4l2 -video_size 800x448 -framerate 30 -i /dev/video2 -c:v h264_v4l2m2m -b:v 8M -c:a copy -an -f rtsp rtsp://localhost:8554/greenhouse -rtsp_transport tcp
exit 0
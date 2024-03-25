#!/bin/bash
./mediamtx &
ffmpeg -input_format yuyv422 -f v4l2 -video_size 864x480 -framerate 24 -i /dev/video2 -c:v h264_v4l2m2m -b:v 1000K -c:a copy -an -f rtsp rtsp://localhost:8554/greenhouse -rtsp_transport tcp
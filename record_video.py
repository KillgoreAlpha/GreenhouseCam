from datetime import datetime, time as dt_time, timedelta
import time
import sys

# Raspberry Pi camera setup
camera = Picamera2()
# Set log date
log_date = datetime.now().strftime("%Y-%m-%d")
# Create log file
log = open(f"/home/bobcat/Videos/Logs/{log_date}.txt", "a")
print("Program started ...", file = log)
# Track number of videos
videos_recorded = 0

# Function to start recording for one hour
def record_video():
    global videos_recorded
    # Get current date and time
    date_str = datetime.now().strftime("%Y-%m-%d_%H%M")
    output_file = f"/home/bobcat/Videos/{date_str}.mp4"
    
    # Start recording
    camera.start_and_record_video(output_file, duration=1800)
    print(f"Recording video to {output_file}...", file = log)
    videos_recorded += 1
    
# Main loop
try:
    while True:
        # Get current time
        current_time = datetime.now().time()

        # Check if it's within the allowed time window
        if dt_time(6, 0) <= current_time <= dt_time(19, 30):
            #(7,30) = 7:30 am (24 hour format, minutes)
            # If it is, start recording for thirty minutes
            record_video()

        # Check if it's before the allowed time window    
        elif dt_time(6, 0) >= current_time:
            print("Recording will begin at 6:00AM...", file = log)
            # Calculate time until next 6:00am
            time_to_record = datetime.combine(datetime.now(), dt_time(6, 0))
            time_to_wait = time_to_record - datetime.now()
            # Sleep until 6:00am
            time.sleep(time_to_wait.total_seconds())
            
        # Otherwise it's after the allowed time window   
        else:
            camera.stop_recording()
            camera.close()
            print(f"Daily recording is complete. {videos_recorded} videos were saved to /home/bobcat/Videos.", file = log)
            print("Program exiting in 60 seconds...", file = log)
            time.sleep(60)
            print("Exiting program...", file = log)
            log.close()
            sys.exit()
            
except KeyboardInterrupt:
    # Stop recording and close the camera gracefully on CTRL+C
    camera.stop_recording()
    camera.close()
    print("Program exited due to user initiation.", file = log)

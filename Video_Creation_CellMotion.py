import cv2
import numpy as np

def generate_synthetic_video(output_path="synthetic_video.mp4", object_type="circle", frame_size=(640, 480),
                             num_objects=5, num_frames=100):
    """
    Generate a synthetic video with moving objects (circles or rectangles).

    :param output_path: Path to save the video.
    :param object_type: Type of object ("circle" or "rectangle").
    :param frame_size: Size of the video frame (width, height).
    :param num_objects: Number of moving objects.
    :param num_frames: Number of frames in the video.
    """
    # Video properties
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    fps = 30
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

    # Initialize object positions and velocities
    positions = np.random.randint(50, min(frame_size) - 50, size=(num_objects, 2))
    velocities = np.random.randint(-5, 5, size=(num_objects, 2))

    for frame_id in range(num_frames):
        # Create a blank frame
        frame = np.zeros((frame_size[1], frame_size[0], 3), dtype=np.uint8)

        for i in range(num_objects):
            # Update positions
            positions[i] += velocities[i]

            # Bounce objects off walls
            for j in range(2):
                if positions[i][j] < 50 or positions[i][j] > frame_size[j] - 50:
                    velocities[i][j] *= -1

            # Draw objects
            if object_type == "circle":
                cv2.circle(frame, tuple(positions[i]), 20, (0, 255, 0), -1)
            elif object_type == "rectangle":
                top_left = (positions[i][0] - 20, positions[i][1] - 20)
                bottom_right = (positions[i][0] + 20, positions[i][1] + 20)
                cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), -1)

        # Write frame to video
        video_writer.write(frame)

    # Release video writer
    video_writer.release()
    print(f"Synthetic video saved to {output_path}")


# Generate synthetic video
generate_synthetic_video(output_path="synthetic_cells.mp4", object_type="circle")
generate_synthetic_video(output_path="synthetic_vehicles.mp4", object_type="rectangle")

# Mouse Behavior Analysis

## Database Testing

```database_tests.ipynb```

    Checks the databaset that we will be working with.

## Scripts

```setup_project.py```

    A Python script to initialize the project environment, set up necessary directories, and configure initial settings.

## Blender file

```paths_for_blender.ipynb```

    Output pdf of paths for rendering in blender (Used for Figure 1). 

## Video Processing

```autopi_video_processing.ipynb```

    Processes raw video files to prepare them for analysis. This includes tasks such as frame extraction, video normalization, and preprocessing steps.

## Mouse Position Extracting


```dlc_training_video_selection.ipynb```

```dlc_mouse_position_prediction.ipynb```

```mouse_position_correct_view1.ipynb```

```mouse_position_create_animal_pose_pose.ipynb```

```mouse_position_fill_positrack_gap_from_arena_top.ipynb```

```lever_pose.ipynb```

```bridge_coordinates_cm.ipynb```

    Mouse position, lever position, arena position, bridge position extraction using DLC.

    The online tracking algorithm is set to minimize false positive at all cost because the data are then passed to the cable actuator.

    For some sessions with positrack2, we have the recorded video that can be used to improve the tracking that was done online.

    We used 2 different camera systems during the autopi task with electrophysiology. The Positrack software tracked infrared LEDs and we also recorded a video of the arena to know the lever position.

    We transformed the position data so that these two systems are aligned.

    The rule is that...

        0,0 is the center of the arena
        The home base relative to the center of the arena is in the direction of 0,-1 vector.
        The values are in cm.

    There are also 2 different reference times. The recording times (duration within ktan .dat files) and ROS time (computers clock).

    To do the analysis, it is simpler if all the data are in the same spatial and temporal reference frame, or if they have both times.

    The animal pose time is usually using the recording time, we added the ROS time for all position data. We save the ROS time in the Animal_pose.pose matrix (7th column).

    The lever position is also calculated for all row of the Animal_pose.pose matrix. This way, we can get the lever position for each trial.

    We need to get the bridge position in the arena-center reference frame. The coordinates should be in cm

    We want to make sure that 0, pi/2, pi, and -pi/2 means the same thing in all our sessions. For instance, does 0 refer to East, North, West or South? We need to have the same reference frame throughout the experiment. 2 tracking systems were used so it is important to check.


## Behavioral Analysis


```behavior_performance.ipynb```

    Behavioral analysis (Figure 1 of the manuscript)









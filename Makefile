INPUT_FILE := input.jpg
SCRIPTS_FOLDER := scripts
OUTPUT_FOLDER := output

.PHONY: all gray hsv right_border bottom_border rotate shift gamma binary contours laplacian_contours clean

all: gray hsv right_border bottom_border rotate shift gamma binary contours laplacian_contours

clean:
	rm $(OUTPUT_FOLDER)/*

gray:
	python3 $(SCRIPTS_FOLDER)/gray.py $(INPUT_FILE) $(OUTPUT_FOLDER)/grayscale.jpg

hsv:
	python3 $(SCRIPTS_FOLDER)/hsv.py $(INPUT_FILE) $(OUTPUT_FOLDER)/hsv.jpg

right_border:
	python3 $(SCRIPTS_FOLDER)/right_border.py $(INPUT_FILE) $(OUTPUT_FOLDER)/flipped_right.jpg

bottom_border:
	python3 $(SCRIPTS_FOLDER)/bottom_border.py $(INPUT_FILE) $(OUTPUT_FOLDER)/flipped_bottom.jpg

rotate:
	python3 $(SCRIPTS_FOLDER)/rotate.py $(INPUT_FILE) $(OUTPUT_FOLDER)/rotated_30_specified_point.jpg

shift:
	python3 $(SCRIPTS_FOLDER)/shift.py $(INPUT_FILE) $(OUTPUT_FOLDER)/shifted_right_10.jpg

gamma:
	python3 $(SCRIPTS_FOLDER)/gamma.py $(INPUT_FILE) $(OUTPUT_FOLDER)/gamma_corrected.jpg

binary:
	python3 $(SCRIPTS_FOLDER)/binary.py $(INPUT_FILE) $(OUTPUT_FOLDER)/binary_thresholded.jpg

contours:
	python3 $(SCRIPTS_FOLDER)/contours.py $(INPUT_FILE) $(OUTPUT_FOLDER)/contours_binary.jpg

laplacian_contours:
	python3 $(SCRIPTS_FOLDER)/laplacian_contours.py $(INPUT_FILE) $(OUTPUT_FOLDER)/laplacian_contours.jpg

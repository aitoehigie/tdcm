# Decode HDD Model number

## Task

Given the image (hc510.png) create a script that will

1. Accept an Ultrastar HDD model number 
2. OCR the image ("How to Read the Ultrastar Model Number")
3. Decode the model number and output the following:
   1. Whether its a helium-filled drive or not
   2. Model capacity in TB
   3. Interface type

## Example output

```bash
$ python main.py HUH721010ALE604
Model number to decode:  HUH721010ALE604
	Helium drive: Yes
	Capacity:     10TB
	Interface:    512e SATA
```




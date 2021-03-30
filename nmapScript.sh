#!/bin/bash
# The script checks if a target is up AND has specific ports open. 
# Script will then scan deeper in the specified targets and sum up the information in an html file.
echo "Please enter the target(s) you wish to scan (using nmap syntax. press -h for reference): "
read -e target

if [ $target == '-h' ]
then
	echo "single target: ip / name"
	echo "number of targets: target1 target2"
	echo "range of targets: x.x.x.x-x.x.x.x"
	echo "network scan: IP/CIDR"
	echo "Please enter the target(s) you wish to scan (using nmap syntax)."
	read -e target
fi

echo "Please specify which ports you wish to scan:"
read -e ports
echo "Please enter the amount of probes, ranging between 0(min) and 9(max):"
read -e intensity
echo "Name the file for your scan:"
read -e fileName
currentFolder=$(pwd)

	
nmap -n -sn $target -oG upAndRunning.txt
grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' upAndRunning.txt > ips.txt
nmap -n -sV --version-intensity $intensity -p $ports -open -iL ips.txt -oX hasPortsOpen.xml
xsltproc hasPortsOpen.xml -o $fileName.html
echo "Scan was completed successfuly. You can see the results at $currentFolder/$fileName.html"

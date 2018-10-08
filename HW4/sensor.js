//Author:Yasir Aslam Shah
//ECEN 5023
//EID 2018 Homework4
//Fall 2018
//Refernce:https://github.com/momenso/node-dht-sensor
//https://www.w3schools.com/js/js_if_else.asp
var sensorLib = require("node-dht-sensor");
//global variables 
var count=0;
var average_temp=0.0;
var average_hum=0.0;
var average_temp1=0.0;
var average_hum1=0.0;
var max_temp=0.0000;
var min_temp=100.0000;
var max_hum=0.0000;
var min_hum=100.0000;
var length="Length:";
var averageT="Average Temperature:";
var averageH="Average Humidity:";
var line='===========================================================';
var sensor = {
	sensors: [ /*{
		name: "Indoor",
		type: 11,
		pin: 17
	}*/, {
		name: "Current Values",
		type: 22,
		pin: 4
	} ],
//read function to read the temperature and humidity values from sensor DHT22
//the values are displayed in unit Ceslsius for temperature and relative percentage for humidity
	read: function() 
		{
		//for loop to extract values from sensor every ten seconds 
		for (var a in this.sensors) 
			{		
				var b = sensorLib.read(this.sensors[a].type, this.sensors[a].pin);
				console.log(this.sensors[a].name + count +": Temperature "
				+b.temperature.toFixed(2) + "°C, Humidity "
				+b.humidity.toFixed(2) + "%");
				//calculting min and max values fro temp and humidity
				if (max_temp < b.temperature.toFixed(2))
					{
						max_temp=b.temperature.toFixed(2);
					}
					if (min_temp > b.temperature.toFixed(2))
					{
						min_temp=b.temperature.toFixed(2);
					}
					if (max_hum < b.humidity.toFixed(2))
					{
						max_hum=b.humidity.toFixed(2);
					}
					if (min_hum > b.humidity.toFixed(2))
					{
						min_hum=b.humidity.toFixed(2);
					}
					average_hum = (b.humidity + average_hum);
					average_temp = (b.temperature + average_temp);
				
				//calculating the average of humidty and temperature for every ten values
				count= count+1;	//counter to keep a value of number of loops			
			}
		setTimeout(function() 	
			{	//function to timeout for ten seconds				
				sensor.read();
			}, 10000);
if(count==10)
{
	average_hum1=average_hum/(10);	//calculating the average value for humidity
	average_temp1= average_temp/(10);//calculating the average value for temperature
	console.log(line);					
	console.log("            Max Temp    :" + max_temp+"°C" +                "\t Max Hum    :" + max_hum+"%");
	console.log("            Min Temp    :" + min_temp+"°C" +                "\t Min Hum    :" + min_hum+"%");
	console.log("            Average Temp:" + average_temp1.toFixed(2)+"°C" +"\t Average Hum:" + average_hum1.toFixed(2)+"%");
	console.log(line);					
	console.log(line);
	console.log("\n");
	//zeroing the average value after averaging every ten values
	average_hum1=0.0;
	average_hum=0.0;
	average_temp=0.0;
	average_temp1=0.0;
	count=0;
}
}
};
sensor.read();

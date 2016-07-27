var weatherData;

function retrieveWeatherData(param, location){
	$.ajax({
		url: 'https://pro.openweathermap.org/data/2.5/' + param + '?q=' + location + '&APPID=dd6d612e24b7d9caa94e93448aaea752',
		type: 'GET',
		dataType: 'jsonp',
		success: function(response){
			weatherData = response;
			if (param === 'weather'){
				displayWeatherData(response);
			}else if(param === 'forecast'){
				displayForecastData(response);
			}

		}
	})
};

function displayWeatherData(){
	var cityName = weatherData.name.replace(' ', '')
	var cityForecast =  $("<ul id=" + cityName + "><h3>" + weatherData.name + "</h3></ul>");
	$("div#forecast").append(cityForecast);
	var degreesF = Math.round((weatherData.main.temp- 273) * 9/5 + 32);
	var temp =  $("<li class='temp'> It is currently " + degreesF + " degrees Fahrenheit in " + weatherData.name + " with " + weatherData.weather[0].description + ".</li>");
    $("ul#" + cityName).append(temp);
}

function displayForecastData(){
	var d = new Date();
	var n = d.getHours();
	var index = Math.round(n/3, 2)
	for (i=index;i<index+3;i++){
		var cityName = weatherData.city.name.replace(' ', '')
		var date = weatherData.list[i].dt_txt.slice(0, 16)
		var description = weatherData.list[i].weather[0].description
		var degreesF = Math.round((weatherData.list[i].main.temp- 273) * 9/5 + 32);
    	var forecast =  $("<li class='temp'>" + date + " -- It will be " + degreesF + " degrees Fahrenheit in " + weatherData.city.name + " with " + description + ".</li>");
    	$("ul#" + cityName).append(forecast);
	}
}

function retrieveWeatherDataForAllLocations(param, locations){
	for (i=0;i<locations.length;i++){
		retrieveWeatherData(param, locations[i])
	}

	retrieveForecastDataForAllLocations('forecast', locations);
}

function retrieveForecastDataForAllLocations(param, locations){
	for (i=0;i<locations.length;i++){
		retrieveWeatherData(param, locations[i])
	}
}

$(function(){
	$("div#forecast").empty()
	var locations = ["Oakland", "San Francisco", "San Jose"];
	retrieveWeatherDataForAllLocations('weather', locations);

})


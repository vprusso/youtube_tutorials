document.addEventListener('DOMContentLoaded', () => {
    const weatherInfoDiv = document.getElementById('weather-info');
    const apiUrl = 'https://api.open-meteo.com/v1/forecast?latitude=50.93333&longitude=6.95&current=temperature_2m,relative_humidity_2m,wind_speed_10m';

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data && data.current) {
                const temperature = data.current.temperature_2m;
                const humidity = data.current.relative_humidity_2m;
                const windSpeed = data.current.wind_speed_10m;

                weatherInfoDiv.innerHTML = `
                    <p>Temperature: ${temperature}°C</p>
                    <p>Humidity: ${humidity}%</p>
                    <p>Wind Speed: ${windSpeed} km/h</p>
                `;
            } else {
                throw new Error('Invalid weather data format');
            }
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
            weatherInfoDiv.innerHTML = '<p>Could not fetch weather data. Please try again later.</p>';
        });
});

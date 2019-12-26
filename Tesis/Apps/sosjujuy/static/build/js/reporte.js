var ctx = document.getElementById('myChart').getContext('2d');
var datos = $('#datos').val();
datos = JSON.parse(datos);
console.log(datos);
var myChart = new Chart(ctx, {
  type: 'bar',
  data: {
      labels: ['Iniciado', 'Enviado', 'Pendiente', 'Anulado', 'Aprobado', 'Rechazado'],
      datasets: [{
          label: '',
          data: datos,
          backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(255, 159, 64, 0.2)'
          ],
          borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(255, 159, 64, 1)'
          ],
          borderWidth: 2
      }]
  },
  options: {
      scales: {
          yAxes: [{
              ticks: {
                  beginAtZero: true
              }
          }]
      }
  }
});
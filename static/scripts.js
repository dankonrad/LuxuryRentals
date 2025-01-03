

// // Feito para desativar o input em caso dos dados forem incorrectos de acordo com o que é inquirido

// (() => {
//     'use strict'
  
//     // Faz a procura de todas as formas que queremos que seja enfluenciada por isso
//     const forms = document.querySelectorAll('.needs-validation')
  
//     // Faz o loop sobre todas as formas, se não estiver de acordo irá para a sua submissão.
//     Array.from(forms).forEach(form => {
//       form.addEventListener('submit', event => {
//         if (!form.checkValidity()) {
//           event.preventDefault()
//           event.stopPropagation()
//         }
  
//         form.classList.add('was-validated')
//       }, false)
//     })  
//   })()



// document.addEventListener('DOMContentLoaded', function() {
//     const priceSlider = document.getElementById('priceSlider');

//     // Initialize noUiSlider
//     noUiSlider.create(priceSlider, {
//         start: [{{ preco_min if preco_min else 0 }}, {{ preco_max if preco_max else 7000 }}],
//         connect: true,
//         range: {
//             'min': 0,
//             'max': 7000
//         },
//         step: 100,
//         tooltips: true,
//         format: {
//             to: value => Math.round(value),
//             from: value => Number(value)
//         }
//     });

//     // Update the display values
//     const minPriceDisplay = document.getElementById('preco_minimo');
//     const maxPriceDisplay = document.getElementById('preco_maximo');

//     priceSlider.noUiSlider.on('update', function(values) {
//         minPriceDisplay.textContent = values[0];
//         maxPriceDisplay.textContent = values[1];
//     });
// });

// function updatePriceRange() {
//   const slider = document.querySelector('#preco_veiculo');
//   const preco_minimo = document.getElementById("preco_minimo").min;
//   const preco_maximo = document.getElementById("preco_maximo").max;

//   const minPrice = slider.value;
//   const maxPrice = 7000;

//   preco_minimo.textContent = minPrice;
//   preco_maximo.textContent = maxPrice;
// }



// document.addEventListener('DOMContentLoaded', updatePriceRange)
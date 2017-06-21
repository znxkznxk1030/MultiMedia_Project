/**
 * Created by znxkz on 2017-06-05.
 */

try {
    // $(document).ready(function () {
    //     Highcharts.setOptions({
    //         global: {
    //             useUTC: false
    //         }
    //     });
    //
    //     var chart;
    //     $('#sound_3d').highcharts({
    //         chart: {
    //             type: 'spline',
    //             animation: Highcharts.svg, // don't animate in old IE
    //             marginRight: 10,
    //             events: {
    //                 load: function () {
    //
    //                     // set up the updating of the chart each second
    //                     var series = this.series[0];
    //                     var series2 = this.series[1];
    //                     var series3 = this.series[2];
    //                     // double buffering problem
    //                     setInterval(function () {
    //                         var _x = (new Date()).getTime(), // current time
    //                             x = x_temp;
    //                         var y = y_temp;
    //                         var z = z_temp;
    //                         series.addPoint([_x, x], false, true);
    //                         series2.addPoint([_x, y], true, true);
    //                         // series3.addPoint([_x, z], true, true);
    //                     }, 1000);
    //                 }
    //             }
    //         },
    //         title: {
    //             text: 'Live random data'
    //         },
    //         xAxis: {
    //             title: {
    //                 text: 'Time(seconds)'
    //             },
    //             type: 'datetime',
    //             tickPixelInterval: 150
    //         },
    //         yAxis: [{
    //             title: {
    //                 text: 'Value'
    //             },
    //             plotLines: [{
    //                 value: 0,
    //                 width: 1,
    //                 color: '#808080'
    //             }]
    //         }],
    //         tooltip: {
    //             formatter: function () {
    //                 return '<b>' + this.series.name + '</b><br/>' +
    //                     Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
    //                     Highcharts.numberFormat(this.y, 2);
    //             }
    //         },
    //         legend: {
    //             enabled: false
    //         },
    //         exporting: {
    //             enabled: false
    //         },
    //         series: [{
    //             name: 'X',
    //             data: (function () {
    //                 // generate an array of random data
    //                 var data = [],
    //                     time = (new Date()).getTime(),
    //                     i;
    //
    //                 for (i = -30; i <= 0; i++) {
    //                     data.push({
    //                         x: time + i * 1000,
    //                         y: 0
    //                     });
    //                 }
    //                 return data;
    //             })()
    //         },
    //             {
    //                 name: 'Y',
    //                 data: (function () {
    //                     // generate an array of random data
    //                     var data = [],
    //                         time = (new Date()).getTime(),
    //                         i;
    //
    //                     for (i = -30; i <= 0; i++) {
    //                         data.push({
    //                             x: time + i * 1000,
    //                             y: 0
    //                         });
    //                     }
    //                     return data;
    //                 })()
    //             },
    //             {
    //                 name: 'Z',
    //                 data: (function () {
    //                     // generate an array of random data
    //                     var data = [],
    //                         time = (new Date()).getTime(),
    //                         i;
    //
    //                     for (i = -30; i <= 0; i++) {
    //                         data.push({
    //                             x: time + i * 1000,
    //                             y: 0
    //                         });
    //                     }
    //                     return data;
    //                 })()
    //             }]
    //     });
    // });
    // $(document).ready(function () {
    //         var panner;
    //         var pattern = 1, speed = 0.05;
    //         var t = 0;
    //         var x, y, z;
    //
    //         init();
    //         initAudio();
    //         animate();
    //
    //         function animate() {
    //             update();
    //         }
    //
    //         function init() {
    //             document.getElementById("speedUp").addEventListener("click", speedUp);
    //             document.getElementById("speedDown").addEventListener("click", speedDown);
    //             document.getElementById("pattern").addEventListener("click", modifyPattern);
    //         }
    //
    //
    //         function initAudio() {
    //             // initialize Audio Context
    //             try {
    //                 var audioContext = new (window.AudioContext || window.webkitAudioContext)();
    //             }
    //             catch (e) {
    //                 alert("Web Audio API is not supported in this browser");
    //             }
    //
    //             // load hrir to the container
    //             var hrtfContainer = new HRTFContainer();
    //             hrtfContainer.loadHrir("../../static/hrir/kemar_L.bin");
    //
    //             // create audio source node from the <audio> element
    //             var sourceNode = audioContext.createMediaElementSource(document.getElementById("player"));
    //             var gain = audioContext.createGain();
    //             gain.gain.value = 0.6;
    //             sourceNode.connect(gain);
    //
    //             // create new hrtf panner, source node gets connected automatically
    //             panner = new HRTFPanner(audioContext, gain, hrtfContainer);
    //
    //             // connect the panner to the destination node
    //             panner.connect(audioContext.destination);
    //             setInterval(updatePanner, 50);
    //             sourceNode.play();
    //         }
    //
    //
    //         function update() {
    //             animateSource();
    //         }
    //
    //         function updatePanner() {
    //
    //             switch (pattern) {
    //                 case 0:
    //                     x = Math.sin(t) * Math.cos(t);
    //                     y = Math.cos(t) * Math.cos(t);
    //                     z = Math.sin(t);
    //                     break;
    //                 case 1:
    //                     x = Math.cos(t);
    //                     y = 0;
    //                     z = Math.sin(t);
    //                     break;
    //                 case 2:
    //                     x = 1;
    //                     y = Math.cos(t);
    //                     z = Math.sin(t);
    //                     break;
    //             }
    //
    //             var cords = cartesianToInteraural(x, y, z);
    //             panner.update(cords.azm, cords.elv);
    //
    //             t += speed;
    //             x_temp = x;
    //             y_temp = y;
    //             z_temp = z;
    //         }
    //
    //         function speedUp() {
    //             var temp = speed;
    //             speed += 0.03;
    //             if (speed > 0.14) {
    //                 speed = temp;
    //             }
    //         }
    //
    //         function speedDown() {
    //             var temp = speed;
    //             speed -= 0.03;
    //             if (speed <= -0.14) {
    //                 speed = temp;
    //             }
    //         }
    //
    //         function modifyPattern() {
    //             pattern = (pattern + 1) % 3;
    //         }
    //     });

} catch (e) {
    alert("Cannot Play on this device");
}
/**
 * Created by znxkz on 2017-06-05.
 */

try {
    window.onload = function () {

        var panner;
        var pattern = 1, speed = 0.05;
        var t = 0;
        var x, y, z;

        init();
        initAudio();
        animate();

        function animate() {
            update();
        }

        function init() {
            document.getElementById("speedUp").addEventListener("click", speedUp);
            document.getElementById("speedDown").addEventListener("click", speedDown);
            document.getElementById("pattern").addEventListener("click", modifyPattern);
        }


        function initAudio() {
            // initialize Audio Context
            try {
                var audioContext = new (window.AudioContext || window.webkitAudioContext)();
            }
            catch (e) {
                alert("Web Audio API is not supported in this browser");
            }

            // load hrir to the container
            var hrtfContainer = new HRTFContainer();
            hrtfContainer.loadHrir("../../static/hrir/kemar_L.bin");

            // create audio source node from the <audio> element
            var sourceNode = audioContext.createMediaElementSource(document.getElementById("player"));
            var gain = audioContext.createGain();
            gain.gain.value = 0.6;
            sourceNode.connect(gain);

            // create new hrtf panner, source node gets connected automatically
            panner = new HRTFPanner(audioContext, gain, hrtfContainer);

            // connect the panner to the destination node
            panner.connect(audioContext.destination);
            setInterval(updatePanner, 50);
            sourceNode.play();
        }


        function update() {
            animateSource();
        }

        function updatePanner() {

            switch (pattern) {
                case 0:
                    x = Math.sin(t) * Math.cos(t);
                    y = Math.cos(t) * Math.cos(t);
                    z = Math.sin(t);
                    break;
                case 1:
                    x = Math.cos(t);
                    y = 0;
                    z = Math.sin(t);
                    break;
                case 2:
                    x = 1;
                    y = Math.cos(t);
                    z = Math.sin(t);
                    break;
            }

            var cords = cartesianToInteraural(x, y, z);
            panner.update(cords.azm, cords.elv);

            t += speed;
        }

        function speedUp() {
            speed += 0.03;
        }

        function speedDown() {
            speed -= 0.03;
        }

        function modifyPattern() {
            pattern = (pattern + 1) % 3;
        }
    }
} catch (e) {
    alert("Cannot Play on this device");
}
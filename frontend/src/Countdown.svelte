<script lang="ts">
  const end = 1652409000000; // friday 13th may 2022 australian time

  let interval = setInterval(update, 1000);

  import { fade } from "svelte/transition";

  export let expired = false;

  let d, h, m, s;
  update();

  function update() {
    // get total seconds between the times
    let delta = end - Date.now();
    expired = delta <= 0;

    delta = Math.abs(delta) / 1000;

    // calculate (and subtract) whole days
    d = Math.floor(delta / 86400);
    delta -= d * 86400;

    // calculate (and subtract) whole hours
    h = Math.floor(delta / 3600) % 24;
    delta -= h * 3600;

    // calculate (and subtract) whole minutes
    m = Math.floor(delta / 60) % 60;
    delta -= m * 60;

    // what's left is seconds
    s = Math.floor(delta % 60); 
  }

  function p(n) {
        return String(n).padStart(2, '0')
  }
</script>

<main>
    <div class="countdown">
        <div class="num">
            {p(d)}    
        </div>
        days
    
        <div class="num">
            {p(h)}    
        </div>
        hours
    
        <div class="num">
            {p(m)}    
        </div>
        minutes
    
        <div class="num">
            {p(s)}    
        </div>
        seconds
    </div>
</main>

<style>
    main {
        padding: 2em;
        border: 3px dashed #333;
        border-radius: 1em;
    }

    .countdown {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 1em;
    }

    .num {
        font-size: xx-large;
        font-family: monospace;
        background-color: #191919;
        padding: 0.5em;
        padding-inline: 0.3em;
        border-radius: 0.25em;
    }
</style>

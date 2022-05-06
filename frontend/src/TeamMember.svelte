<script lang="ts">
    import MdClose from 'svelte-icons/md/MdClose.svelte'

    let name: string;
    let year: number = 11;
    let mg: number = 0;
    let discord: string;
    let ign: string;

    let error: string | null = null;

    function validate() {
        if (!(/^[a-zA-Z]+ [a-zA-Z]+$/i.test(name))) {
            return "Full Name Required"
        }

        if (!(year >= 7 && year <= 12)) {
            return "Invalid Year Level"
        }

        if (!(mg >= 0 && mg <= 13)) {
            return "Invalid Mentor Group"
        }

        if (!(/^.{3,32}#[0-9]{4}$/.test(discord))) {
            return "Invalid Discord Tag"
        }

        if (ign.length == 0) {
            return "Please enter your in-game name"
        }

        return null;
    }

    function onChange() {
        error = validate()
    }
</script>


<div class="adder">
    <div class="close">
        <MdClose />
    </div>
    <label for="name">Real Name</label>
    <input type="text" name="name" placeholder="eg. Martin Velikov" bind:value={name} on:change={onChange}>

    <div class="mg_container">
        <div>
            <label for="year">Year Level</label>
            <input type="number" name="year" min="7" max="12" bind:value={year} on:change={onChange}>
        </div>

        <span class="mg_dot">
            .
        </span>

        <div>
            <label for="mg">Mentor Group</label>
            <input type="number" name="mg" min="0" max="13" bind:value={mg} on:change={onChange}>
        </div>
    </div>

    <label for="discord">Discord Tag</label>
    <input type="text" name="discord" placeholder="eg. codian#1724" bind:value={discord} on:change={onChange}>

    <label for="ign">In Game Username</label>
    <input type="text" name="ign" placeholder="eg. Codian" bind:value={ign} on:change={onChange}>

    {#if error != null}
        <div class="error">
            <span class="error-icon">
                <MdClose />
            </span>
            <span>
                {error}
            </span>
        </div>
    {/if}
</div>

<style>
    .adder {
        position: relative;
        padding: 1em;
        width: min-content;
        background-color: #333;
        border-radius: 0.5em;
        box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
    }

    label {
        font-weight: bold;
        padding-block: 0.5em;
        min-width: max-content;
    }

    input {
        width: 100%;
        flex-grow: 1;
    }

    .mg_container {
        display: flex; 
        gap: 0.5em;
        width: 100%;
    }

    .mg_container > div {
        flex-grow: 1;
    }

    .mg_dot {
        align-self: flex-end;
        padding-block: 0.25em;
        font-weight: bold;
        font-size: xx-large;
    }

    .close {
        position: absolute;
        width: 1em;
        right: 0.5em;
        top: 0.5em;
        cursor: pointer;
    }

    .close:hover {
        color: orangered;
    }

    .error {
        color: orange;
        height: min-content;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .error-icon {
        height: 32px;
    }
</style>
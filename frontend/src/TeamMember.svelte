<script lang="ts">
    import MdClose from 'svelte-icons/md/MdClose.svelte'
    import MdWarning from 'svelte-icons/md/MdWarning.svelte'

    export let name: string;
    export let year: number;
    export let mg: number;
    export let discord: string;
    export let ign: string;
    export let sub: boolean;

    import { createEventDispatcher } from 'svelte';
    const dispatch = createEventDispatcher();

    let error: string | null = validate();
    
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
            return "Please Enter IGN"
        }

        return null;
    }

    function onChange() {
        error = validate()
        dispatch('change',
            { name, year, mg, discord, ign, sub, valid: (error === null) }
        );
    }

    function onRemove() {
        dispatch('remove')
    }
</script>


<div class="adder">
    <div class="close" on:click={onRemove}>
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

    <span class="oneline">
        <label for="sub">Is Subsititute Player</label>
        <span class="spring" />
        <input type="checkbox" name="sub" placeholder="Substitute" bind:checked={sub} on:change={onChange}>
    </span>

    {#if error !== null}
        <div class="error">
            <span class="error-icon">
                <MdWarning />
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
    
    input:not([type='checkbox']) {
        width: 100%;
        flex-grow: 1;
    }


    .oneline {
        display: flex;
        align-items: center;
    }
    
    .spring {
        flex-grow: 1;
    }
</style>
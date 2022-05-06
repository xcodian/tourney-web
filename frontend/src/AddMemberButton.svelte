<script lang="ts">
    import { createEventDispatcher } from 'svelte';

    import MdAddCircle from 'svelte-icons/md/MdAddCircle.svelte'

    const dispatch = createEventDispatcher();
</script>

<div class="add" on:click={() => dispatch('click')}>
    <div class="icon">
        <MdAddCircle />
    </div>

    <span>Add</span>
</div>

<style>
    .add {
        color: dodgerblue;
        border: 2px dashed #666;
        border-radius: 1em;
        
        user-select: none;
        cursor: pointer;
        
        box-sizing: border-box;
        padding: 1em;
        margin-inline: 1em;
        
        box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
    }

    .icon {
        height: 32px;
        margin-bottom: 0.25em;
    }
</style>
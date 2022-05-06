<script lang="ts">
import TeamMember from "./TeamMember.svelte";
</script>

<main>
	<h1>Your Team</h1>
	<div class="roster">
		<TeamMember />
		<TeamMember />
		<TeamMember />
		<TeamMember />
	</div>
</main>

<style>
	.roster {
		display: flex;
		gap: 1em;
	}
</style>
<script lang="ts">
	import TeamMember from "./TeamMember.svelte";
	import AddMemberButton from "./AddMemberButton.svelte";

	import MdWarning from 'svelte-icons/md/MdWarning.svelte'

	import { fade, scale } from 'svelte/transition';
	import { flip } from 'svelte/animate';
	import { onMount } from "svelte";

	const MAX_NONSUBS = 5;
	const MIN_NONSUBS = 5;
	let members = [];
	let non_subs = [];
	let team_name = ""

	let error: string | null = "initial";

	$: non_subs = members.filter(x => !x.sub);
	$: members, team_name, error = validateWholeTeam();

	function addNewMember() {
		members.push({
			name: "",
			discord: "",
			ign: "",
			mg: 0,
			year: 11,
			sub: non_subs.length >= MAX_NONSUBS,
			valid: false,
		})

		members = members;
	}

	function removeMember(member) {
		members = members.filter(x => x != member);
	}

	function validateWholeTeam() {
		if (!(/^[a-z0-9 ]+$/i.test(team_name))) {
			return "Your team name is invalid."
		}

		if (non_subs.length > MAX_NONSUBS) {
			return `You can have a maximum of ${MAX_NONSUBS} non-sub players. (You have ${non_subs.length})`;
		}

		if (non_subs.length < MIN_NONSUBS) {
			return `You need at least ${MIN_NONSUBS} non-sub players. (You have ${non_subs.length})`;
		}

		if (members.some(x => !x.valid)) {
			return `Some team member data seems to be incomplete or invalid.`;
		}

		return null;
	}

	function submit() {
		
	}
</script>

<main class="flex">
	<br>
	<img src="GamingPlusLogo.svg" height="128" alt="GIHS Gaming+ Logo">
	<h1>GIHS Gaming+ Tournament Sign Up</h1>
	<p>Please enter your team's details below.</p>

	{#if error == null}
		<br><br>
		<h1>You're all set!</h1>
		<p>Please note that submitting is irreversible.</p>
		<p>You can't edit your team's data later.</p>
		<br>
		<button class="submit" on:click={submit}>
			Submit
		</button>
	{/if}

	<br><br>
	<label for="teamname">Team Name</label>
    <input type="text" name="teamname" placeholder="eg. Red Team" bind:value={team_name} on:change={validateWholeTeam}>

	<br>
	{#if error != null}
		<div class="error" transition:fade>
			<span class="error-icon">
				<MdWarning />
			</span>
			<span>
				{error}
			</span>
		</div>
	{/if}

	<br><br>
	<h2>Your Players {(non_subs.length != members.length) ? `(${members.length - non_subs.length} subs)` : ""}</h2>
	<div class="roster">
		{#each members as member}
			<div class="flex">
				<TeamMember
					name={member.name}
					discord={member.discord}
					ign={member.ign} 
					mg={member.mg}
					year={member.year}
					sub={member.sub}
					on:change={({ detail }) => member = detail}
					on:remove={() => removeMember(member)}
				/>
			</div>
		{/each}
		<AddMemberButton on:click={addNewMember} />
	</div>
</main>

<style>
	.flex {
		display: flex;
		align-items: center;
		justify-content: center;
	}

	main {
		flex-direction: column;
	}
	.roster {
		display: flex;
		align-items: center;
		gap: 1em;
		flex-wrap: wrap;
		padding: 1em;
	}
</style>
<script lang="ts">
	import TeamMember from "./TeamMember.svelte";
	import AddMemberButton from "./AddMemberButton.svelte";
	import Countdown from "./Countdown.svelte";

	import MdWarning from 'svelte-icons/md/MdWarning.svelte'

	import { fade, scale } from 'svelte/transition';
	import { flip } from 'svelte/animate';
	import { onMount } from "svelte";

	const MAX_NONSUBS = 5;
	const MIN_NONSUBS = 5;
	let members = [];
	let non_subs = [];
	let name = ""

	let submitting = false;
	let submitted = false;
	let error: string | null = "initial";
	let allowTryAgain = false;
	let expired = false;

	$: non_subs = members.filter(x => !x.sub);
	$: members, name, error = validateWholeTeam();

	function addNewMember() {
		members.push({
			name: "",
			discord: "",
			ign: "",
			mg: 0,
			year: 11,
			sub: non_subs.length >= MAX_NONSUBS,
			valid: false
		})

		members = members;
	}

	function removeMember(member) {
		members = members.filter(x => x != member);
	}

	function validateWholeTeam() {
		allowTryAgain = false;

		if (name.length === 0) {
			return "Get started by picking a team name!"
		} else if (!(/^[a-z0-9 ]+$/i.test(name))) {
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

	async function submit() {
		submitting = true;
		try {
			const response = await fetch('/api/register', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({ name, members })
			});

			switch(response.status) {
				case 409:
					error = "This team name has already been registered."
					break;
				case 400:
					error = "Invalid data submitted."
					break;
				case 500:
					error = "Server error while submitting, please try again later. Report this error to admins."
					allowTryAgain = true;
					break;
				default:
					error = "Unknown error while submitting: " + response.status + " " + response.statusText;
					allowTryAgain = true;
					break;
				case 200:
					submitted = true;
					break;
			}
		} catch (e) {
			console.error(e);
		} finally {
			submitting = false;
		}
	}
</script>

<main class="flex">
	<br>
	<img src="GamingPlusLogo.svg" height="128" alt="GIHS Gaming+ Logo">
	<h1>GIHS Gaming+ Tournament Sign Up</h1>

	{#if !expired}
		{#if submitted}
			<br><br>
			<h2 class="green">Your team has been registered.</h2>
			<p>You may now close this tab. Good luck to {name} in the tournament!</p>
		{:else}
			<p>Please enter your team's details below.</p>
			<br>
			<Countdown bind:expired={expired} />
		{/if}

		
		{#if error == null && !submitted}
			<br><br>
			<h1 class="green">Ready to go?</h1>
			<p class="green">Please note that submitting is irreversible.</p>
			<p class="green">You can't edit your team's data later.</p>
			<br>
			<button class="submit" on:click={submit}>
				Sign My Team Up!
			</button>
		{/if}

		{#if !submitting && !submitted}
			<br><br>
			<h2>Your Team Name</h2>
			<input type="text" name="teamname" placeholder="eg. Red Team" bind:value={name} on:change={validateWholeTeam}>

			<br>
			{#if error != null}
				<div class="error" transition:fade>
					<span class="error-icon">
						<MdWarning />
					</span>
					<span>
						{error}
					</span>

					{#if allowTryAgain}
						<!-- svelte-ignore a11y-missing-attribute -->
						<a on:click={submit} style="padding-left: 10px;">Try Again</a>
					{/if}
				</div>
			{/if}

			<br>
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
		{/if}
	{:else}
		<br><br>
		<h2 class="red">Sign-ups for the tournament have ended!</h2>
		<p>All playing teams have been registered and finalized.</p>
	{/if}
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
		padding: 0.5em;
	}

	.green {
		color: lightgreen;
	}

	.red {
		color: lightcoral;
	}
</style>
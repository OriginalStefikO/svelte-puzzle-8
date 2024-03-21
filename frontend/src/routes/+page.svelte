<svelte:head>
	<title>Puzzle 8</title>
	<meta name="description" content="Puzzle 8 solver" />
</svelte:head>

<script lang="ts">
	import ButtonPrimary from "$lib/components/ButtonPrimary.svelte";
import Puzzle8Solver from "$lib/components/Puzzle8Solver.svelte";
	import SolutionCarousel from "$lib/components/SolutionCarousel.svelte";
	import { onMount } from "svelte";
	import axios from "axios";
	import { puzzleGoalMatrix, puzzleStartMatrix, solverResponse } from "$lib/stores";
	import PuzzleMatrix from "$lib/components/PuzzleMatrix.svelte";
	import { dev } from '$app/environment';

	// const route_base = 'http://localhost:8200/v1/dummy';
	// const route_dummy = 'http://localhost:8080/v1/dummy';

	const axios_instance = axios.create({
		baseURL: "http://localhost:8080/v1/",
	});

	onMount(() => {
		const searchParams = new URLSearchParams(window.location.search);
		const inputString = searchParams.get("inputString");

		puzzleStartMatrix.set(inputString || "123456780");
	});

	function solve() {
		console.log("Solving...");
		
		if (dev) {
			console.log($puzzleStartMatrix);
			console.log($puzzleGoalMatrix);
		}

		axios_instance.post("/solver", null, { params:{
			start_state: $puzzleStartMatrix,
			goal_state: $puzzleGoalMatrix
		}}).then((response) => {
			if (dev) {
				console.log(response.data);
			}
			solverResponse.set(response.data)
		}).catch((error) => {
			console.error(error);
		});
	}
</script>

<div class="flex flex-col items-center gap-4">
  <Puzzle8Solver inputString={$puzzleStartMatrix} />

	<ButtonPrimary onClick={solve}>
		Solve!
	</ButtonPrimary>

	{#if $solverResponse != undefined}
		<section class="flex flex-col gap-2 my-2">
		<div class="flex flex-col gap-2">
			<p class="text-center">Time taken: {$solverResponse.time_taken.toFixed(2)}s</p>
			<p class="text-center">Nodes expanded: {$solverResponse.total_nodes_expanded}</p>
		</div>

		{#if $solverResponse.status_code == 200}
			<SolutionCarousel>
				{#each $solverResponse.solution.reverse() as matrix, index}
					<div id={`solution-carousel-${index}`} class="relative bg-primary bg-opacity-35 items-center gap-2 flex flex-col p-2 rounded-xl w-fit h-fit opacity-25">
						<div class="m-2 mb-0">
							<PuzzleMatrix puzzleMatrix={matrix.state} />
						</div>
							
						<div class="flex gap-2 mx-1">
							<p class="whitespace-nowrap text-sm">G: {matrix.g}</p>
							<p class="whitespace-nowrap text-sm">H: {matrix.h}</p>
							<p class="whitespace-nowrap text-sm">F: {matrix.f}</p>
						</div>
					</div>
				{/each}
			</SolutionCarousel>
		{:else}
			<p class="text-center">{$solverResponse.message}</p>
		{/if}
		</section>
	{/if}
</div>
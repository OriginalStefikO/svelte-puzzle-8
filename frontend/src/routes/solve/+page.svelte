<svelte:head>
	<title>Puzzle 8</title>
	<meta name="description" content="Puzzle 8 solver" />
</svelte:head>

<script lang="ts">
	import Puzzle8Solver from "$lib/components/Puzzle8Solver.svelte";
	import { onMount } from "svelte";
	
  $: data = {
		inputString: "123456780"
	};

	onMount(() => {
		const searchParams = new URLSearchParams(window.location.search);
		const inputString = searchParams.get("inputString");

		data = {
			inputString: inputString || "123456780",
		};
	});
</script>

<div>
  <Puzzle8Solver inputString={data.inputString} />
</div>
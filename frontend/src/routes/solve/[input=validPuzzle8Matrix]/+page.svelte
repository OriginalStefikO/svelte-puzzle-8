<svelte:head>
	<title>Puzzle 8</title>
	<meta name="description" content="Puzzle 8 solver" />
</svelte:head>

<script lang="ts">
	import Puzzle8Solver from "$lib/components/Puzzle8Solver.svelte";
	import type { PageData } from "./$types";

  export let data: PageData;
</script>

<div>
  <Puzzle8Solver inputString={data.inputString} />
</div>
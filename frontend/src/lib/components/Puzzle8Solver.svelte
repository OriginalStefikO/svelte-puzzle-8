<script lang="ts">
  import ArrowRight from 'lucide-svelte/icons/arrow-right';

	import { convertStringToMatrix as stringToMatrix } from '$lib/scripts/convert';
	import { checkInputString } from '$lib/scripts/regex';
	import { puzzleGoalMatrix, puzzleStartMatrix } from '$lib/stores';
	import PuzzleMatrix from './PuzzleMatrix.svelte';

	export let inputString: string = '';
  export let outputString: string = '123456780';
  puzzleStartMatrix.set(inputString);
  puzzleGoalMatrix.set(outputString);

	function inputFieldChange(e: Event & { currentTarget: EventTarget & HTMLInputElement }) {
		const target = e.target as HTMLInputElement;
    target.value = target.value.replace(/[^0-8]/g, '');

    if (target.value.length > 9) {
      target.value = target.value.slice(0, 9);
    }

    let currentString = inputString;

    if (target.id !== 'inputString') {
      currentString = outputString;
    }
    
    if (!checkInputString(currentString)) { return; }
    
    target.classList.remove('border-b-2', 'border-b-red-500');
    const resultMatrix = target.value;

    if (target.id === 'inputString') {
      puzzleStartMatrix.update(() => resultMatrix);
    } else {
      puzzleGoalMatrix.update(() => resultMatrix);
    }
	}
</script>

<div class="min-w-36 w-fit min-h-24 h-fit p-3 bg-primary bg-opacity-35 rounded-lg flex justify-between gap-3">
  <!-- Left input pane -->
	<section class="flex flex-col gap-2 text-text">
    <div class="flex flex-col">
      <label for="inputString" class="text-sm italic">Input string</label>
      <input
        id="inputString"
        type="text"
        class="h-8 rounded-lg border border-gray-400 p-2 text-background"
        placeholder="123456780"
        bind:value={inputString}
        on:input={(e) => inputFieldChange(e)}
      />
    </div>

    <div class="flex flex-col">
      <label for="outputString" class="text-sm italic">Output string</label>
      <input
        id="outputString"
        type="text"
        class="h-8 rounded-lg border border-gray-400 p-2 text-background"
        placeholder="123456780"
        bind:value={outputString}
        on:input={(e) => inputFieldChange(e)}
      />
    </div>
	</section>

	<div class="w-0.5 bg-primary bg-opacity-20"></div>

	<section class="flex gap-2 items-center">
		<PuzzleMatrix puzzleMatrix={stringToMatrix($puzzleStartMatrix)} />

    <ArrowRight class="stroke-accent" />

    <PuzzleMatrix puzzleMatrix={stringToMatrix($puzzleGoalMatrix)} />
	</section>
</div>

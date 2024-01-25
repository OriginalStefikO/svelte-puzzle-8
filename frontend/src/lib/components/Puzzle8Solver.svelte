<script lang="ts">
	import { convertStringToMatrix } from '$lib/scripts/convert';
	import { checkInputString } from '$lib/scripts/regex';
	import { puzzleMatrix } from '$lib/stores';
	import PuzzleMatrix from './PuzzleMatrix.svelte';

	export let inputString: string = '';
  export let outputString: string = '';
  puzzleMatrix.set(convertStringToMatrix(inputString));

	function inputFieldChange(e: Event & { currentTarget: EventTarget & HTMLInputElement }) {
		const target = e.target as HTMLInputElement;
    target.value = target.value.replace(/[^0-8]/g, '');

    if (target.value.length > 9) {
      target.value = target.value.slice(0, 9);
    }

    if (!checkInputString(inputString)) { return; }
    
    target.classList.remove('border-b-2', 'border-b-red-500');
    const resultMatrix = convertStringToMatrix(target.value);
    puzzleMatrix.update(() => resultMatrix);
	}
</script>

<div class="min-w-36 w-fit min-h-24 h-fit p-3 bg-gray-200 rounded-lg flex justify-between gap-3">
  <!-- Left input pane -->
	<section class="flex flex-col gap-2">
    <div class="flex flex-col">
      <label for="inputString" class="text-sm italic">Input string</label>
      <input
        id="inputString"
        type="text"
        class="h-8 rounded-lg border border-gray-400 p-2"
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
        class="h-8 rounded-lg border border-gray-400 p-2"
        placeholder="123456780"
        bind:value={outputString}
        on:input={(e) => inputFieldChange(e)}
      />
    </div>
	</section>

	<div class="w-0.5 bg-gray-400"></div>

  <!-- Right output pane -->
	<section>
		<PuzzleMatrix />
	</section>
</div>

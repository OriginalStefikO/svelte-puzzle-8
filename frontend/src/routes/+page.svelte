<svelte:head>
	<title>Home</title>
	<meta name="description" content="Home screen and Puzzle 8 solver" />
</svelte:head>

<script lang="ts">
	import { checkInputString } from "$lib/scripts/regex";

	let inputString:string = '';
	let inputField: HTMLInputElement;

	function inputFieldChange(e: Event & { currentTarget: EventTarget & HTMLInputElement }) {
		const target = e.target as HTMLInputElement;
		target.value = target.value.replace(/[^0-8]/g, '');

		if (target.value.length > 9) {
			target.value = target.value.slice(0, 9);
		}

		inputField.classList.remove('border-b-2', 'border-b-red-500')
	}

	function startSolving() {
		inputString = inputString.replace(/[^0-8]/g, '');

		if (inputString.length == 0) {
			window.location.href = '/solve';
		}
		else if (checkInputString(inputString)) {
			window.location.href = `/solve/${inputString}`;
		} else {
			alert('Invalid input string!');
			inputField.classList.add('border-b-2', 'border-b-red-500');
		}
	}
</script>

<div class="flex flex-col items-center gap-2">
	<input
		type="text"
		class="w-full rounded-lg border border-gray-400 px-2 py-1 focus:outline-none focus:border-blue-500"
		placeholder="123456780"
		on:input={(e) => inputFieldChange(e)}
		bind:value={inputString}
		bind:this={inputField}
	/>

	<button class="w-fit h-fit bg-blue-500 py-3 px-5 rounded-xl text-white font-bold" on:click={startSolving}>
		Start solving!
	</button>
</div>

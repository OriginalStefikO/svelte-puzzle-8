import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const prerender = false;

export const load: PageLoad = ({ params }) => {
	if (params.input) {
    console.log(params.input);
		return { 
      inputString: params.input,
    }
	}

  // TODO - this should check if solvable
	error(404, 'Not found');
};

import { writable, type Writable } from "svelte/store";
import type { PuzzleResponse } from "./types/object_types";

export const puzzleStartMatrix: Writable<string> = writable("123456780");

export const puzzleGoalMatrix: Writable<string> = writable("123456780");

export const solverResponse: Writable<PuzzleResponse> = writable()
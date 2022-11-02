<script setup lang="ts">
 
</script>

<template>
 <div>
	<h1>{{matriz}}</h1>
 </div>
</template>

<style>
</style>

<script lang="ts">
export default {
	data() {
		return {
			matriz: Array(10).fill(0).map(()=>Array(10).fill(0))
		}
	},
	methods:
	{
		printmatriz() {
			for (let index = 0; index <= this.matriz[30][30]; index++) {
				let element = this.matriz[index];
			}
		}
	}
	
}
</script>
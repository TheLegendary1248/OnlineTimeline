<script>
	import heko from '$lib/test.year.month.day.json'
	let scrollerdate = '';
	let stringifyFunc = (heko) => JSON.stringify(heko,null,"\xa0\xa0\xa0\xa0")
</script>

<svelte:head>
	<title>OnlineTimeline</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<h1 hidden="true">Welcome to Online Timeline</h1>
	<div style="position: relative; width: 600px; height: 600px;">
		<div id="timeline-scrollerview">
			<nav>	
				<input bind:value={scrollerdate} type="date">
			</nav>
			<pre id="container">
				{stringifyFunc(heko)}
			</pre>
		</div>
	</div>
	
</section>

<style>
	#timeline-scrollerview {
		position: absolute;
		border: 5px solid darkblue;
		min-width: 100px;
		width: 100%;
		min-height: 100px;
		height: 100%;
	}
	#container {
		white-space: pre-line;
	}
	nav {
		background-color: #fff;
		min-height: 50px;
	}
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}
</style>

chrome.commands.onCommand.addListener(
	function(action) {
		console.log('Blocked:', action);
	}
);
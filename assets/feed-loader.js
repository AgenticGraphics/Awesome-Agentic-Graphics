/* JSON is the only feed source: merged data needs no generated JS update. */
window.feedReady = (async function () {
  try {
    const response = await fetch(new URL('data/daily-results.json', document.baseURI), {cache:'no-store'});
    if (!response.ok) throw new Error('Feed request failed');
    const daily = await response.json();
    window.FeedValidation.validate(daily);
    window.SURVEY_DATA.daily = daily;
  } catch (error) {
    window.SURVEY_DATA.daily = null;
    console.warn('Daily feed unavailable; reload to retry.');
  }
})();

// Every route on this site is static (no per-request data), so prerender at build time.
// The generated HTML is uploaded as a Workers static asset and served without ever
// invoking the Worker script. Remove this if a route ever needs SSR.
export const prerender = true;

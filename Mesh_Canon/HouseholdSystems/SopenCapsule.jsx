export default function RoxyHouseholdMesh() {
  const sopen = {
    name: "SOPEN (Substance Overdose Prevention & Education Network)",
    short: "SOPEN Hamilton / GTHA",
    mission:
      "Volunteer-led, community-based harm reduction education and mutual aid focused on the toxic drug crisis in the Greater Toronto & Hamilton Area (GTHA).",
    vision: [
      "A world without overdose-related deaths",
      "Drug policy rooted in public health and human rights",
      "Decriminalization and regulated safe supply",
      "Stigma-free, compassionate healthcare"
    ],
    hashtags: ["#CarryYourKitCampaign", "#HarmReduction", "#NaloxoneSavesLives"],
    links: {
      site: "https://sopen.org/",
      carryYourKit: "https://sopen.org/carryyourkitcampaign/",
      instagram: "https://www.instagram.com/SOPENhamilton"
    },
    actions: [
      { label: "Carry Your Kit", href: "https://sopen.org/carryyourkitcampaign/" },
      { label: "Book a Presentation", href: "https://sopen.org/book-a-presentation/" },
      { label: "Community Resources", href: "https://sopen.org/community-resources/" },
      { label: "Get Involved", href: "https://sopen.org/" }
    ]
  };

  // Minimal local state for household-facing utilities
  const starterTodos = [
    {
      id: 1,
      text: "Confirm how many naloxone kits are in the household & car",
      done: false
    },
    {
      id: 2,
      text: "Check expiration dates; schedule resupply if < 60 days",
      done: false
    },
    { id: 3, text: "Identify three nearby training locations", done: false },
    {
      id: 4,
      text: "Add SOPEN contact + presentation date to calendar",
      done: false
    }
  ];

  const attestationHint =
    "e.g., ‘Met Alex at the Stinson community fridge; gave them a kit and showed the rescue breaths card. Follow-up next week.’";

  return (
    <div className="min-h-screen w-full bg-neutral-50 text-neutral-900">
      {/* Header */}
      <header className="sticky top-0 z-10 bg-white/80 backdrop-blur border-b border-neutral-200">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="h-10 w-10 rounded-2xl bg-neutral-900 text-white grid place-items-center text-sm font-semibold">
              RM
            </div>
            <div>
              <h1 className="text-xl font-semibold">Roxy’s Household Mesh</h1>
              <p className="text-xs text-neutral-500">v0.1 • SOPEN Capsule</p>
            </div>
          </div>
          <div className="hidden md:flex items-center gap-3 text-sm">
            {sopen.hashtags.map((h) => (
              <span
                key={h}
                className="px-2 py-1 rounded-full bg-neutral-100 border border-neutral-200"
              >
                {h}
              </span>
            ))}
          </div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 py-6 grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Org Summary Card */}
        <section className="lg:col-span-2 bg-white rounded-2xl shadow-sm border border-neutral-200 p-5">
          <div className="flex items-start justify-between gap-4">
            <div>
              <h2 className="text-lg font-semibold">{sopen.name}</h2>
              <p className="mt-1 text-sm text-neutral-600">{sopen.mission}</p>
            </div>
            <a
              href={sopen.links.site}
              target="_blank"
              rel="noreferrer"
              className="text-sm px-3 py-2 rounded-xl border border-neutral-300 hover:bg-neutral-50"
            >
              Visit site ↗
            </a>
          </div>

          <div className="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="bg-neutral-50 rounded-xl p-4 border border-neutral-200">
              <h3 className="font-medium">Vision Anchors</h3>
              <ul className="mt-2 space-y-1 list-disc list-inside text-sm text-neutral-700">
                {sopen.vision.map((v, i) => (
                  <li key={i}>{v}</li>
                ))}
              </ul>
            </div>
            <div className="bg-neutral-50 rounded-xl p-4 border border-neutral-200">
              <h3 className="font-medium">Quick Actions</h3>
              <div className="mt-2 grid grid-cols-1 sm:grid-cols-2 gap-2">
                {sopen.actions.map((a) => (
                  <a
                    key={a.label}
                    href={a.href}
                    target="_blank"
                    rel="noreferrer"
                    className="text-sm px-3 py-2 rounded-xl border border-neutral-300 bg-white hover:bg-neutral-50 text-center"
                  >
                    {a.label} ↗
                  </a>
                ))}
              </div>
            </div>
          </div>
        </section>

        {/* Kit Tracker */}
        <section className="bg-white rounded-2xl shadow-sm border border-neutral-200 p-5">
          <h2 className="text-lg font-semibold">Naloxone Kit Tracker</h2>
          <p className="mt-1 text-sm text-neutral-600">
            Record household kit count, locations, and expiry dates. Create a
            simple cadence: check monthly; replace at < 60 days.
          </p>
          <div className="mt-4 space-y-2">
            <label className="block text-sm">Kits on hand</label>
            <input
              type="number"
              defaultValue={2}
              className="w-full border border-neutral-300 rounded-xl px-3 py-2 text-sm"
            />
            <label className="block text-sm mt-3">Notes</label>
            <textarea
              placeholder="Car glovebox (1), Kitchen drawer (1). Alex carries 1."
              className="w-full border border-neutral-300 rounded-xl px-3 py-2 text-sm h-20"
            />
            <button className="w-full mt-3 text-sm px-3 py-2 rounded-xl border border-neutral-300 bg-neutral-900 text-white hover:opacity-90">
              Save kit status
            </button>
          </div>
        </section>

        {/* Attestation & Field Notes */}
        <section className="lg:col-span-2 bg-white rounded-2xl shadow-sm border border-neutral-200 p-5">
          <h2 className="text-lg font-semibold">Attestations & Field Notes</h2>
          <p className="mt-1 text-sm text-neutral-600">
            Capture small, verifiable stories of care and contact. These become
            the backbone of our local mesh memory.
          </p>
          <div className="mt-3 grid grid-cols-1 md:grid-cols-3 gap-3">
            <input
              className="border border-neutral-300 rounded-xl px-3 py-2 text-sm"
              placeholder="Who/where? (optional)"
            />
            <input
              className="border border-neutral-300 rounded-xl px-3 py-2 text-sm"
              placeholder="What was offered/received?"
            />
            <input
              className="border border-neutral-300 rounded-xl px-3 py-2 text-sm"
              placeholder="Follow-up date (optional)"
            />
          </div>
          <textarea
            className="w-full mt-3 border border-neutral-300 rounded-xl px-3 py-2 text-sm h-24"
            placeholder={attestationHint}
          />
          <div className="mt-3 flex gap-2">
            <button className="text-sm px-3 py-2 rounded-xl border border-neutral-300 bg-white hover:bg-neutral-50">
              Save note
            </button>
            <button className="text-sm px-3 py-2 rounded-xl border border-neutral-300 bg-white hover:bg-neutral-50">
              Share with SOPEN liaison
            </button>
          </div>
        </section>

        {/* To‑Do / Setup Checklist */}
        <section className="bg-white rounded-2xl shadow-sm border border-neutral-200 p-5">
          <h2 className="text-lg font-semibold">Setup Checklist</h2>
          <ul className="mt-2 space-y-2">
            {starterTodos.map((t) => (
              <li key={t.id} className="flex items-start gap-2">
                <input type="checkbox" className="mt-1" />
                <span className="text-sm">{t.text}</span>
              </li>
            ))}
          </ul>
          <div className="mt-4 flex gap-2">
            <input
              className="flex-1 border border-neutral-300 rounded-xl px-3 py-2 text-sm"
              placeholder="Add next action…"
            />
            <button className="text-sm px-3 py-2 rounded-xl border border-neutral-300 bg-white hover:bg-neutral-50">
              Add
            </button>
          </div>
        </section>

        {/* Add Another Org Capsule (placeholder) */}
        <section className="lg:col-span-3 bg-white rounded-2xl shadow-sm border border-neutral-200 p-5">
          <h2 className="text-lg font-semibold">Add another Org Capsule</h2>
          <p className="mt-1 text-sm text-neutral-600">
            As Roxy’s mesh grows, capture each org’s mission, actions, and a
            few household‑level workflows (e.g., kit checks, event visits,
            donation cadence).
          </p>
          <div className="mt-3 grid grid-cols-1 md:grid-cols-4 gap-3">
            <input className="border border-neutral-300 rounded-xl px-3 py-2 text-sm" placeholder="Org name" />
            <input className="border border-neutral-300 rounded-xl px-3 py-2 text-sm" placeholder="Website" />
            <input className="border border-neutral-300 rounded-xl px-3 py-2 text-sm" placeholder="Primary action link" />
            <button className="text-sm px-3 py-2 rounded-xl border border-neutral-300 bg-neutral-900 text-white hover:opacity-90">
              Create capsule
            </button>
          </div>
        </section>
      </main>

      <footer className="max-w-6xl mx-auto px-4 pb-10 text-xs text-neutral-500">
        Built with love for Roxy • Household Mesh v0.1
      </footer>
    </div>
  );
}

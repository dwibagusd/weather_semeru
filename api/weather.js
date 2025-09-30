export default async function handler(req, res) {
  try {
    const response = await fetch("https://meteojuanda.id/share/api-semeru/aws.json", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });

    if (!response.ok) {
      throw new Error(`Fetch failed: ${response.status}`);
    }

    const data = await response.json();

    res.setHeader("Content-Type", "application/json");
    res.setHeader("Cache-Control", "public, max-age=60"); // cache 1 menit
    res.status(200).json(data);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
}

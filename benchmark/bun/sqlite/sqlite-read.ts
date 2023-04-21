import { Database } from "bun:sqlite";

const db = new Database("benchmark/DB/chinook.sqlite")
const query = db.query(`SELECT albums.Title, artists.Name, SUM(invoice_items.Quantity) AS total_sales
    FROM albums
    JOIN artists ON albums.ArtistId = artists.ArtistId
    JOIN tracks ON tracks.AlbumId = albums.AlbumId
    JOIN invoice_items ON invoice_items.TrackId = tracks.TrackId
    GROUP BY albums.AlbumId
    ORDER BY total_sales DESC`);

const query2 = db.query(`SELECT media_types.Name, COUNT(tracks.TrackId) AS total_tracks
    FROM media_types
    JOIN tracks ON media_types.MediaTypeId = tracks.MediaTypeId
    GROUP BY media_types.Name;`);

console.log(query.all())
console.log(query2.all())

db.close()

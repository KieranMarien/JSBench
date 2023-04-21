import { DB } from "https://deno.land/x/sqlite/mod.ts";

const db = new DB('benchmark/DB/chinook.sqlite' , { mode: "read" })

const query1 = db.query(`SELECT media_types.Name, COUNT(tracks.TrackId) AS total_tracks
    FROM media_types
    JOIN tracks ON media_types.MediaTypeId = tracks.MediaTypeId
    GROUP BY media_types.Name;`);

const query2 = db.query(`SELECT albums.Title, artists.Name, SUM(invoice_items.Quantity) AS total_sales
    FROM albums
    JOIN artists ON albums.ArtistId = artists.ArtistId
    JOIN tracks ON tracks.AlbumId = albums.AlbumId
    JOIN invoice_items ON invoice_items.TrackId = tracks.TrackId
    GROUP BY albums.AlbumId
    ORDER BY total_sales DESC`);

console.log(query1)
console.log(query2)
db.close()



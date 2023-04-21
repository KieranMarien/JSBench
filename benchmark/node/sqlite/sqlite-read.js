const Database = require('better-sqlite3');
const path = require('path')

const db = new Database(path.join("benchmark/DB/chinook.sqlite"));

const query1 =
  db.prepare(`SELECT media_types.Name, COUNT(tracks.TrackId) AS total_tracks
      FROM media_types
      JOIN tracks ON media_types.MediaTypeId = tracks.MediaTypeId
      GROUP BY media_types.Name;`).all()
console.log(query1)




const query2 =
  db.prepare(`SELECT albums.Title, artists.Name, SUM(invoice_items.Quantity) AS total_sales
      FROM albums
      JOIN artists ON albums.ArtistId = artists.ArtistId
      JOIN tracks ON tracks.AlbumId = albums.AlbumId
      JOIN invoice_items ON invoice_items.TrackId = tracks.TrackId
      GROUP BY albums.AlbumId
      ORDER BY total_sales DESC`).all()
console.log(query2)

db.close()

import 'package:flutter/material.dart';

class Menu extends StatefulWidget {
  const Menu({super.key});

  @override
  State<Menu> createState() => _MenuState();
}

class _MenuState extends State<Menu> {
  @override
  Widget build(BuildContext context) {
    final List<String> items = <String>['Vincent Van Gogh','Pablo Picasso','Claude Monet', 'Leonardo da Vinci'];
    return Container(
        padding: const EdgeInsets.all(16.0),
        decoration: const BoxDecoration(
          color: Colors.red,
          borderRadius: BorderRadius.all(Radius.circular(15))
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            const Padding(
              padding: EdgeInsets.fromLTRB(8, 0, 8, 0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text("Art Style Transfer Project", style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold)),
                    Text("Dinali Assylbek", style: TextStyle(fontSize: 25, fontWeight: FontWeight.bold)),
                    Text("CS 4640", style: TextStyle(fontSize: 25, fontWeight: FontWeight.bold)),
                  ],
                ),
            ),
            const Spacer(),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Padding(
                  padding: EdgeInsets.all(8.0),
                  child: Text("Pick and Artist", style: TextStyle(fontSize: 18)),
                ),
                DropdownButtonFormField(
                  decoration: InputDecoration(
                      border: const OutlineInputBorder(borderRadius:BorderRadius.all(Radius.circular(15.0)),
                      ),
                      filled: true,
                      hintStyle: TextStyle(color: Colors.grey[800]),
                      fillColor: Colors.white,
                  ),
                  onChanged: (value) {},
                  items: items.map((String item) {
                    return DropdownMenuItem<String>(
                      value: item,
                      child: Text(item)
                    );
                  }).toList(),
                ),
              ],
            ),
            Column(
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Padding(
                      padding: EdgeInsets.all(8.0),
                      child: Text("Select A File", style: TextStyle(fontSize: 18)),
                    ),
                    IconButton(
                      onPressed: () {}, 
                      icon: const Icon(Icons.attach_file)
                    )
                  ],
                ),
                Container(
                  height: MediaQuery.of(context).size.height / 3,
                  width: double.infinity,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(15),
                    color: Colors.white
                  ),
                  child: const Center(child: Text("No Image Selected")),
                )
              ],
            ),
            const Spacer(),
            SizedBox(
              width: double.infinity,  // Makes the button fill the width
              height: 50,
              child: ElevatedButton(
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.white,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(15)
                  )
                ),
                onPressed: () {},
                child: const Text('Transfer'),
              ),
            ),
          ],
        )
    );
  }
}
import text
import view
import model

my_Note = model.Note()

def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                my_Note.open()
                view.print_message(text.load_successful)
            case 2:
                my_Note.save()
                view.print_message(text.save_successful)
            case 3:
                pb = my_Note.load()
                view.print_note(pb, text.note_empty)
                # my_pb.show()
            case 4:
                contact = view.input_note(text.input_new_note)
                name = my_Note.add(contact)
                view.print_message(text.new_note_successful(name))
            case 5:
                key_word = view.input_search(text.input_search)
                result = my_Note.search(key_word)
                view.print_note(result, text.empty_search(key_word))
            case 6:
                key_word = view.input_search(text.input_change)
                result = my_Note.search(key_word)
                if result:
                    if len(result) != 1:
                        view.print_note(result, '')
                        current_id = view.input_search(text.input_index)
                    else:
                        current_id = result[0].get('id')
                    new_contact = view.input_note(text.change_note)
                    name = my_Note.change(new_contact, current_id)
                    view.print_message(text.change_successful(name))
                else:
                    view.print_message(text.empty_search(key_word))

            case 7:
                index = view.input_search(text.input_change)
                result = my_Note.delete(index)
                view.print_note(result, text.delete_successful(index))
            case 8:
                break

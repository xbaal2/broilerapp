import json, os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.animation import Animation
from kivy.utils import get_color_from_hex # Import untuk warna

KONTRAK_FILE = "kontrak.json"

# ===============================
# ICON BUTTONS DENGAN SIZE FLEXIBLE
# ===============================
class IconButton(ButtonBehavior, BoxLayout):
    def __init__(self, icon_path, text, width=200, height=50, **kwargs):
        super().__init__(orientation='horizontal', spacing=5, padding=5, **kwargs)
        self.size_hint = (None, None)
        self.width = width
        self.height = height
        self.icon = Image(source=icon_path, size_hint=(None, 1), width=32)
        self.label = Label(text=text, halign='left', valign='middle', color=(1,1,1,1))
        self.label.bind(size=self.label.setter('text_size'))
        self.add_widget(self.icon)
        self.add_widget(self.label)

class IconToggleButton(ToggleButton, BoxLayout):
    def __init__(self, icon_path, text, width=150, height=70, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = 5
        self.padding = 5
        self.size_hint = (None, None)
        self.width = width
        self.height = height
        self.icon = Image(source=icon_path, size_hint=(None, 1), width=32)
        self.label = Label(text=text, halign='left', valign='middle', color=(1,1,1,1))
        self.label.bind(size=self.label.setter('text_size'))
        self.add_widget(self.icon)
        self.add_widget(self.label)

# ===============================
# TOMBOL TIMBUL DENGAN SHADOW + ANIMASI
# ===============================
class RaisedIconButton(IconButton):
    def __init__(self, icon_path, text, width=200, height=50, **kwargs):
        super().__init__(icon_path, text, width, height, **kwargs)
        self.bg_color_normal = get_color_from_hex('#3498DB')  # Biru
        self.bg_color_pressed = get_color_from_hex('#2980B9') # Biru tua
        
        with self.canvas.before:
            # Shadow di bawah tombol
            self.shadow_color = Color(0, 0, 0, 0.25)
            self.shadow_rect = RoundedRectangle(pos=(self.x+3, self.y-3), size=self.size, radius=[10])
            # Background tombol
            self.bg_color = Color(*self.bg_color_normal)
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
        self.shadow_rect.pos = (self.x+3, self.y-3)
        self.shadow_rect.size = self.size

    def on_press(self):
        # Animasi penekanan tombol
        self.bg_color.rgba = self.bg_color_pressed
        anim = Animation(pos=(self.x+2, self.y-2), duration=0.05)
        anim.start(self)

    def on_release(self):
        # Animasi pelepasan tombol
        self.bg_color.rgba = self.bg_color_normal
        anim = Animation(pos=(self.x-2, self.y+2), duration=0.05)
        anim.start(self)

# ===============================
# POPUP FUNGSIONAL DENGAN DESAIN ICONIC
# ===============================
def show_popup(title, message):
    # Tentukan ikon berdasarkan judul (sesuai permintaan user: warning.png dan done.png)
    if "Error" in title or "[ERROR]" in message:
        icon_path = "icons/warning.png"
        icon_size = (64, 64)
        bg_color = get_color_from_hex('#FF5733') # Merah untuk error
    elif "Sukses" in title:
        icon_path = "icons/done.png" # Menggunakan done.png untuk sukses
        icon_size = (64, 64)
        bg_color = get_color_from_hex('#2ECC71') # Hijau untuk sukses
    else:
        icon_path = "icons/doc.png"
        icon_size = (64, 64)
        bg_color = get_color_from_hex('#3498DB') # Biru default

    # Konten utama Popup
    content = BoxLayout(orientation='vertical', spacing=15, padding=15)
    
    # Tambahkan latar belakang untuk konten popup
    with content.canvas.before:
        Color(*bg_color)
        RoundedRectangle(pos=content.pos, size=content.size, radius=[15])

    # 1. Ikon
    icon = Image(source=icon_path, size_hint=(None, None), size=icon_size)
    icon_box = BoxLayout(size_hint_y=None, height=icon_size[1], padding=0)
    icon_box.add_widget(Widget())
    icon_box.add_widget(icon)
    icon_box.add_widget(Widget())
    
    # 2. Judul (di bawah ikon)
    title_label = Label(text=title, font_size=30, color=(1,1,1,1), size_hint_y=None, height=30)
    
    # 3. Pesan (di bawah judul)
    message_label = Label(text=message, font_size=26, color=(1,1,1,1), halign='center', valign='middle')
    message_label.bind(size=message_label.setter('text_size'))
    
    # 4. Tombol OK
    # Menggunakan ikon "check.png" yang generik untuk tombol OK
    close_button = RaisedIconButton(icon_path="icons/check.png", text="OK", width=100, height=45) 
    
    btn_box = BoxLayout(size_hint_y=None, height=50)
    btn_box.add_widget(Widget())
    btn_box.add_widget(close_button)
    btn_box.add_widget(Widget())
    
    # Susun konten
    content.add_widget(icon_box)
    content.add_widget(title_label)
    content.add_widget(message_label)
    content.add_widget(btn_box)

    # Popup itu sendiri
    popup = Popup(title='', # Hilangkan judul bawaan
                  content=content, 
                  size_hint=(0.85, 0.45), 
                  auto_dismiss=False,
                  separator_height=0) # Hilangkan garis pemisah judul
    
    # Bind tombol untuk menutup popup
    close_button.bind(on_release=popup.dismiss)
    popup.open()


# ===============================
# APLIKASI BROILER
# ===============================
class BroilerApp(App):
    def build(self):
        self.kontrak_data = self.load_kontrak()
        root_layout = BoxLayout(orientation='vertical', spacing=5, padding=5)

        # ===============================
        # HEADER (LOGO + NAMA APLIKASI)
        # ===============================
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=90, padding=0, spacing=0)
        
        # Pengaturan warna latar belakang melalui Canvas:
        with header.canvas.before:
            Color(0, 0, 0, 1) # Set warna menjadi Hitam
            self.header_rect = RoundedRectangle(size=header.size, pos=header.pos)
        header.bind(pos=self.update_header_rect, size=self.update_header_rect)

        # PERBAIKAN LOGO: keep_ratio=True untuk menghindari distorsi
        logo_image = Image(source="icons/logo.png", 
                           size_hint=(1, 1), 
                           allow_stretch=True, 
                           keep_ratio=True) # <-- FIX: Mempertahankan rasio aspek
        
        header.add_widget(logo_image)
        root_layout.add_widget(header)

        # ===============================
        # TAB BAR
        # ===============================
        tab_bar = BoxLayout(orientation='horizontal', size_hint_y=None, height=80, spacing=5)
        self.btn_kontrak = IconToggleButton("icons/doc.png", "KONTRAK", group="tabs", width=160, height=70)
        self.btn_input   = IconToggleButton("icons/chart.png", "INPUT DATA", group="tabs", width=120, height=70)
        self.btn_hasil   = IconToggleButton("icons/money.png", "HASIL", group="tabs", width=110, height=70)

        tab_bar.add_widget(self.btn_kontrak)
        tab_bar.add_widget(Widget())
        tab_bar.add_widget(self.btn_input)
        tab_bar.add_widget(Widget())
        tab_bar.add_widget(self.btn_hasil)
        root_layout.add_widget(tab_bar)

        # CONTENT AREA
        self.content_area = BoxLayout()
        root_layout.add_widget(self.content_area)

        # ===============================
        # KONTRAK LAYOUT
        # ===============================
        self.kontrak_layout = ScrollView()
        kontrak_inner = BoxLayout(orientation='vertical', size_hint_y=None, spacing=15, padding=15)
        kontrak_inner.bind(minimum_height=kontrak_inner.setter('height'))
        self.kontrak_inputs = {}

        kontrak_fields = {
            "harga_doc": "Harga DOC per ekor",
            "harga_vaksin": "Harga vaksin per ekor",
            "harga_ovk": "Harga OVK per ekor",
        }
        grid_main = GridLayout(cols=2, size_hint_y=None, row_default_height=45, spacing=10)
        grid_main.bind(minimum_height=grid_main.setter('height'))
        for key, label in kontrak_fields.items():
            grid_main.add_widget(Label(text=label))
            ti = TextInput(multiline=False)
            if key in self.kontrak_data:
                ti.text = str(self.kontrak_data[key])
            self.kontrak_inputs[key] = ti
            grid_main.add_widget(ti)
        kontrak_inner.add_widget(grid_main)

        # Harga Pakan
        kontrak_inner.add_widget(Label(text="Harga Pakan (kg):", size_hint_y=None, height=35))
        grid_pakan = GridLayout(cols=2, size_hint_y=None, row_default_height=45, spacing=10)
        grid_pakan.bind(minimum_height=grid_pakan.setter('height'))
        self.kontrak_inputs["harga_pakan"] = {}
        for key in ["pre_starter", "starter_1", "starter_2"]:
            grid_pakan.add_widget(Label(text=key))
            ti = TextInput(multiline=False)
            if "harga_pakan" in self.kontrak_data and key in self.kontrak_data["harga_pakan"]:
                ti.text = str(self.kontrak_data["harga_pakan"][key])
            self.kontrak_inputs["harga_pakan"][key] = ti
            grid_pakan.add_widget(ti)
        kontrak_inner.add_widget(grid_pakan)

        # Bonus IP
        kontrak_inner.add_widget(Label(text="Bonus IP (contoh: IP>=320 -> 150):", size_hint_y=None, height=35))
        grid_bonus = GridLayout(cols=2, size_hint_y=None, row_default_height=45, spacing=10)
        grid_bonus.bind(minimum_height=grid_bonus.setter('height'))
        self.kontrak_inputs["bonus_ip"] = {}
        for key in ["320", "301", "290"]:
            grid_bonus.add_widget(Label(text=f"IP >= {key}"))
            ti = TextInput(multiline=False)
            if "bonus_ip" in self.kontrak_data and key in self.kontrak_data["bonus_ip"]:
                ti.text = str(self.kontrak_data["bonus_ip"][key])
            self.kontrak_inputs["bonus_ip"][key] = ti
            grid_bonus.add_widget(ti)
        kontrak_inner.add_widget(grid_bonus)

        # Harga Jual
        kontrak_inner.add_widget(Label(text="Harga Jual per kg:", size_hint_y=None, height=35))
        grid_jual = GridLayout(cols=2, size_hint_y=None, row_default_height=45, spacing=10)
        grid_jual.bind(minimum_height=grid_jual.setter('height'))
        self.kontrak_inputs["harga_jual"] = {}
        jual_keys = [
            "0.8-0.99","1.0-1.19","1.2-1.39","1.4-1.59","1.6-1.69",
            "1.7-1.79","1.8-1.89","1.9-1.99","2.0-2.09","2.1-2.19","2.2+"
        ]
        for key in jual_keys:
            grid_jual.add_widget(Label(text=f"{key} kg"))
            ti = TextInput(multiline=False)
            if "harga_jual" in self.kontrak_data and key in self.kontrak_data["harga_jual"]:
                ti.text = str(self.kontrak_data["harga_jual"][key])
            self.kontrak_inputs["harga_jual"][key] = ti
            grid_jual.add_widget(ti)
        kontrak_inner.add_widget(grid_jual)

        # Tombol Simpan (timbul)
        self.btn_simpan = RaisedIconButton("icons/save.png", "Simpan Kontrak", width=200, height=100)
        self.btn_simpan.bind(on_press=self.simpan_kontrak)
        kontrak_inner.add_widget(self.btn_simpan)

        self.kontrak_layout.add_widget(kontrak_inner)

        # ===============================
        # INPUT PERFORMA LAYOUT
        # ===============================
        self.input_layout = ScrollView()
        input_inner = BoxLayout(orientation='vertical', size_hint_y=None, spacing=15, padding=15)
        input_inner.bind(minimum_height=input_inner.setter('height'))

        self.inputs = {}
        performa_fields = [
            "Umur panen (hari)",
            "Jumlah DOC awal",
            "Jumlah mati total",
            "Bobot total panen (kg)",
            "Total pakan (kg)"
        ]
        grid_input = GridLayout(cols=2, size_hint_y=None, row_default_height=45, spacing=10)
        grid_input.bind(minimum_height=grid_input.setter('height'))
        for field in performa_fields:
            grid_input.add_widget(Label(text=field))
            ti = TextInput(multiline=False)
            self.inputs[field] = ti
            grid_input.add_widget(ti)
        input_inner.add_widget(grid_input)

        # Tombol Hitung (timbul)
        self.btn_hitung = RaisedIconButton("icons/money.png", "Hitung Laba & Performa", width=250, height=100)
        self.btn_hitung.bind(on_press=self.hitung)
        input_inner.add_widget(self.btn_hitung)

        self.input_layout.add_widget(input_inner)

        # ===============================
        # HASIL LAYOUT
        # ===============================
        self.hasil_layout = ScrollView()
        hasil_inner = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10, padding=15)
        hasil_inner.bind(minimum_height=hasil_inner.setter('height'))

        self.result_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=5)
        self.result_layout.bind(minimum_height=self.result_layout.setter('height'))

        hasil_inner.add_widget(self.result_layout)
        self.hasil_layout.add_widget(hasil_inner)

        # ===============================
        # SWITCH TAB
        # ===============================
        def switch_tab(instance):
            self.content_area.clear_widgets()
            if instance == self.btn_kontrak:
                self.content_area.add_widget(self.kontrak_layout)
            elif instance == self.btn_input:
                self.content_area.add_widget(self.input_layout)
            elif instance == self.btn_hasil:
                self.content_area.add_widget(self.hasil_layout)

        self.btn_kontrak.bind(on_press=switch_tab)
        self.btn_input.bind(on_press=switch_tab)
        self.btn_hasil.bind(on_press=switch_tab)

        self.btn_kontrak.state = 'down'
        self.content_area.add_widget(self.kontrak_layout)

        # agar TF tidak tertutup keyboard
        Window.softinput_mode = 'below_target'

        # ===============================
        # FOOTER
        # ===============================
        footer = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
        footer.add_widget(Label(text="Created by iqbalyda", font_size=18, halign='center'))
        root_layout.add_widget(footer)

        return root_layout
    
    def update_header_rect(self, instance, value):
        # Digunakan untuk memperbarui posisi latar belakang header (warna hitam)
        self.header_rect.pos = instance.pos
        self.header_rect.size = instance.size

    # =========================
    # SIMPAN & MUAT KONTRAK
    # =========================
    def load_kontrak(self):
        if os.path.exists(KONTRAK_FILE):
            try:
                with open(KONTRAK_FILE, "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading {KONTRAK_FILE}: {e}")
                return {}
        return {}

    def simpan_kontrak(self, instance):
        try:
            data = {
                "harga_doc": float(self.kontrak_inputs["harga_doc"].text or 0),
                "harga_vaksin": float(self.kontrak_inputs["harga_vaksin"].text or 0),
                "harga_ovk": float(self.kontrak_inputs["harga_ovk"].text or 0),
                "harga_pakan": {},
                "bonus_ip": {},
                "harga_jual": {}
            }
            for k, v in self.kontrak_inputs["harga_pakan"].items():
                data["harga_pakan"][k] = float(v.text or 0)
            for k, v in self.kontrak_inputs["bonus_ip"].items():
                data["bonus_ip"][k] = float(v.text or 0)
            for k, v in self.kontrak_inputs["harga_jual"].items():
                data["harga_jual"][k] = float(v.text or 0)
            with open(KONTRAK_FILE, "w") as f:
                json.dump(data, f, indent=2)
            self.result_layout.clear_widgets()
            self.add_hasil_row("icons/save.png", "Kontrak berhasil disimpan!")
            # Menggunakan show_popup dengan title "Sukses" -> pakai done.png
            show_popup("Sukses", "Kontrak berhasil disimpan!") 
        except Exception as e:
            self.result_layout.clear_widgets()
            self.add_hasil_row("icons/warning.png", f"[ERROR] {str(e)}")
            # Menggunakan show_popup dengan title "Error" -> pakai warning.png
            show_popup("Error", f"Gagal menyimpan kontrak: {e}") 

    # =========================
    # HELPER UNTUK HASIL DENGAN ICON
    # =========================
    def add_hasil_row(self, icon_file, text):
        row = BoxLayout(orientation='horizontal', size_hint_y=None, height=35, spacing=5)
        row.add_widget(Image(source=icon_file, size_hint=(None, 1), width=32))
        lbl = Label(text=text, halign='left', valign='middle')
        lbl.bind(size=lbl.setter('text_size'))
        row.add_widget(lbl)
        self.result_layout.add_widget(row)

    # =========================
    # HITUNG PERFORMA & LABA
    # =========================
    def hitung(self, instance):
        try:
            if not os.path.exists(KONTRAK_FILE):
                self.result_layout.clear_widgets()
                self.add_hasil_row("icons/warning.png", "[ERROR] Kontrak belum disimpan!")
                # Menggunakan show_popup dengan title "Error" -> pakai warning.png
                show_popup("Error", "Kontrak belum disimpan!") 
                return
            with open(KONTRAK_FILE, "r") as f:
                kontrak = json.load(f)

            # Validasi dan konversi input
            umur = float(self.inputs["Umur panen (hari)"].text.replace(",", ".") or 0)
            jumlah_awal = int(self.inputs["Jumlah DOC awal"].text or 0)
            jumlah_mati = int(self.inputs["Jumlah mati total"].text or 0)
            bobot_total = float(self.inputs["Bobot total panen (kg)"].text.replace(",", ".") or 0)
            total_pakan = float(self.inputs["Total pakan (kg)"].text.replace(",", ".") or 0)

            if jumlah_awal == 0 or (jumlah_awal - jumlah_mati) <= 0 or bobot_total == 0 or total_pakan == 0:
                self.result_layout.clear_widgets()
                self.add_hasil_row("icons/warning.png", "[ERROR] Input tidak valid. Cek semua angka.")
                # Menggunakan show_popup dengan title "Error" -> pakai warning.png
                show_popup("Error", "Input tidak valid. Pastikan semua kolom input data performa diisi dengan benar.") 
                return

            bobot_rata = bobot_total / (jumlah_awal - jumlah_mati)
            mortalitas = (jumlah_mati / jumlah_awal) * 100
            fcr = total_pakan / bobot_total
            # Menghindari pembagian oleh nol
            if umur == 0 or fcr == 0:
                ip = 0
            else:
                ip = (bobot_rata * 100 * (100 - mortalitas)) / (umur * fcr)

            harga_jual = 0
            # Cari harga jual berdasarkan bobot rata-rata
            for k, v in kontrak["harga_jual"].items():
                if "+" in k:
                    try:
                        batas = float(k.replace("+", ""))
                        if bobot_rata >= batas:
                            harga_jual = v
                    except ValueError:
                        continue
                elif "-" in k:
                    try:
                        low, high = map(float, k.split("-"))
                        if low <= bobot_rata <= high:
                            harga_jual = v
                    except ValueError:
                        continue
            
            # Jika tidak ada range yang cocok, set default (misalnya 22000)
            if harga_jual == 0:
                harga_jual = 22000


            bonus_ip = 0
            # Cari bonus IP
            sorted_bonus_keys = sorted([float(k) for k in kontrak["bonus_ip"].keys()], reverse=True)
            for batas in sorted_bonus_keys:
                if ip >= batas:
                    # Karena kunci di kontrak adalah string integer ("320"), pastikan konversi yang benar
                    bonus_ip = kontrak["bonus_ip"][str(int(batas))]
                    break

            # Perhitungan Biaya dan Pendapatan
            harga_doc = kontrak.get("harga_doc", 0)
            vaksin = kontrak.get("harga_vaksin", 0)
            ovk = kontrak.get("harga_ovk", 0)
            
            # Asumsi komposisi pakan (dapat disesuaikan jika ada data riil)
            porsi_pre = total_pakan * 0.05
            porsi_1 = total_pakan * 0.25
            porsi_2 = total_pakan * 0.70

            pre = kontrak["harga_pakan"].get("pre_starter", 0)
            s1 = kontrak["harga_pakan"].get("starter_1", 0)
            s2 = kontrak["harga_pakan"].get("starter_2", 0)

            biaya_total = (harga_doc + vaksin + ovk) * jumlah_awal + (porsi_pre * pre) + (porsi_1 * s1) + (porsi_2 * s2)
            harga_jual_akhir = harga_jual + bonus_ip
            pendapatan = bobot_total * harga_jual_akhir
            laba_total = pendapatan - biaya_total
            
            # Laba per ekor
            if jumlah_awal > 0:
                laba_per_ekor = laba_total / jumlah_awal
            else:
                laba_per_ekor = 0

            # Tampilkan Hasil
            self.result_layout.clear_widgets()
            self.add_hasil_row("icons/chicken.png", f"Bobot rata-rata        : {bobot_rata:,.3f} kg/ekor")
            self.add_hasil_row("icons/chart.png", f"FCR                           : {fcr:,.3f}")
            self.add_hasil_row("icons/money.png", f"IP                               : {ip:,.2f}")
            self.add_hasil_row("icons/skull.png", f"Mortalitas.               : {mortalitas:,.2f} %")
            self.add_hasil_row("icons/money.png", f"Harga jual                 : Rp {harga_jual:,.0f}/kg")
            self.add_hasil_row("icons/trophy.png", f"Bonus IP                   : Rp {bonus_ip:,.0f}/kg")
            self.add_hasil_row("icons/money.png", f"Harga jual total       : Rp {harga_jual_akhir:,.0f}/kg")
            self.add_hasil_row("icons/moneybag.png", f"Pendapatan total    : Rp {pendapatan:,.0f}")
            self.add_hasil_row("icons/receipt.png", f"Total biaya               : Rp {biaya_total:,.0f}")
            self.add_hasil_row("icons/profit.png", f"Laba total                 : Rp {laba_total:,.0f}")
            self.add_hasil_row("icons/chick.png", f"Laba per ekor           : Rp {laba_per_ekor:,.0f}")

            if ip >= 400:
                self.add_hasil_row("icons/star.png", "Performa sangat bagus!")
            elif ip >= 300:
                self.add_hasil_row("icons/star.png", "Performa baik.")
            else:
                self.add_hasil_row("icons/warning.png", "Performa perlu ditingkatkan.")

            # Menggunakan show_popup dengan title "Hasil Hitung" (akan default ke 'doc.png' atau bisa dicek dengan 'Sukses')
            show_popup("Sukses Hitung", "Performa & Laba berhasil dihitung!") 

        except ValueError:
            self.result_layout.clear_widgets()
            self.add_hasil_row("icons/warning.png", "[ERROR] Pastikan semua input berupa angka yang valid.")
            # Menggunakan show_popup dengan title "Error" -> pakai warning.png
            show_popup("Error", "Kesalahan Input: Pastikan semua kolom input performa diisi dengan angka yang valid.")
        except Exception as e:
            self.result_layout.clear_widgets()
            self.add_hasil_row("icons/warning.png", f"[ERROR] Terjadi kesalahan tak terduga: {str(e)}")
            # Menggunakan show_popup dengan title "Error" -> pakai warning.png
            show_popup("Error", f"Terjadi kesalahan tak terduga: {e}")

if __name__ == "__main__":
    BroilerApp().run()
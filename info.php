<h1>Pierwsza strona w PHP</h1>


<?php //znacznik otwierający php
    //phpinfo();
    print_r($_POST);
?>
<!-- znacznik zamykający php -->


<h2>Informacje nt. wersji PHP</h2>
<form name="formularz" id="formularz" method="POST">
      <table class="table">
        <tr>
          <td><label for="imie">Imię</label></td>
          <td><input type="text" name="imie" value=""></td>
        </tr>
        <tr>
          <td><label for="nazwisko">Nazwisko</label></td>
          <td><input type="text" name="nazwisko" value=""></td>
        </tr>
      </table>

      <fieldset>
        <legend >Wybierz płeć</legend>
         <input type="radio" name="gender" value="m"> Mężczyzna<br>
         <input type="radio" name="gender" value="k"> Kobieta<br>
         <input type="radio" name="gender" value="i" checked> Inna
      </fieldset>

      <fieldset>
        <legend>Wybierz pojazd</legend>
        <input type="checkbox" name="vehicle1" value="Bike"> I have a bike<br>
        <input type="checkbox" name="vehicle2" value="Car"> I have a car
      </fieldset>

      <select name="cars">
        <option value="volvo">Volvo</option>
        <option value="saab">Saab</option>
        <option value="fiat" selected>Fiat</option>
        <option value="audi">Audi</option>
      </select>

      <select name="cars2" multiple>
        <option value="volvo">Volvo</option>
        <option value="saab">Saab</option>
        <option value="fiat" selected>Fiat</option>
        <option value="audi">Audi</option>
      </select>

      <br>
      <textarea name="message" rows="10" cols="30">Mój kot.</textarea>
      <br>

      <input type="submit" name="" value="Prześlij">
      <input type="reset" name="" value="Resetuj">

</form>

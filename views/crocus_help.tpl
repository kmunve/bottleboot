

<div class="panel panel-default">
  <div class="panel-body">
<p>
Snøskredvarslingen bruker snødekkemodellen Surfex/Crocus for å simulere utviklingen av snødekkets oppbygning gjennom sesongen. Surfex/Crocus blir utviklet og vedlikeholdt av snøforskningsinstituttet CEN i Grenoble som er en del av Meteo France.
Modellen trenger følgende meteorologiske parameter som inngangsdata:
</p>

<ul>
	<li>lufttemperatur</li>
	<li>luftfuktighet (spesifikk)</li>
	<li>lufttrykk</li>
	<li>vindhastighet</li>
	<li>innkommende kort- og langbølge stråling</li>
	<li>nedbørsrate delt opp i regn og snø</li>
</ul>
<p>
Ideelt måles disse verdier minst hver time på en automatisk værstasjon som står på et representativt sted. Det er få værstasjoner i Norge som måler alle nødvendige inngangsparameter og enda mindre som gjør dette med riktig tidsoppløsning. Faktisk er det ingen :-)
</p>
<p>
Løsninger er at vi henter manglende observasjoner fra værmodellen AROME-MetCoop, som er den operative værmodellen som ligger f.eks. bak yr.no. Modellen "drives" altså med en kombinasjon av observerte og modellerte værdata.
</p>
<p>
Som du kan tenke deg vel dette i seg selv allerede åpne for muligheten at snødekkemodellen kan være feil. Måler en sensor ved stasjonen feil eller er verdien vi henter fra værmodellen feil vil dette medføre følgefeil i snødekkemodellen. Ved siden av disse følgefeilene gjennom inngangsdata har også selve modellen noen svakheter.
</p>
<ul>
	<li>Vanndreneringen av smeltevann eller regn blir simulerte på en veldig enkelt og ofte urealistisk måte som fører til at modellen ofte vil vise alt for tykke skare og islag. Dette jobbes faktisk for tiden med og vi håper at vanndreneringen vil bli bedre modellerte neste sesong.</li>
	<li>Selv om vind er en inngangsparameter brukes det for tiden kun for å beregne korrekt varmefluksene på snøoverflaten og mekanisk omvandling av snøoverflaten. Modellen ikke tar hensyn til erosjon eller deposisjon av vindtransportert snø.</li>
	<li>Snøkrystaller som fordamper eller kondenserer på snøoverflaten blir trukket fra eller lagt til det øverste laget i snødekket. Dette med samme egenskaper som det allerede eksisterende laget. Kort fortalt betyr dette at Crocus for tiden ikke kan modellere dannelsen av overflaterim.</li>
</ul>
<p>
Nok med de dårlige nyheter. Modellen ventes å være nyttig for å følge med på utviklingen av snødekke i regioner der vi ellers har lite observasjoner eller for å anslå utbredelsen av en punktobservasjon. Nysnømengde, setting, ev. vindpakning bør simuleres korrekte så lenge inngangsparameterne er ikke gale. Start og slutt av vanntilførsel gjennom regn eller snøsmelting bør være nyttig. Modellen bør kunne brukes til å følge med på oppbygning av kantkorn og begerkrystaller.
</p>
<p>
Vi håper at denne siden hjelper dere litt til å ta i bruk snødekkemodeller i varslings- og/eller observatørarbeidet deres. Får å få modellene bedre er vi avhengig av å samle inn erfaringen med når modellen virker eller er på villspor. Har du en "case" eller en observasjoner som illustrerer dette, eller et spørsmål ta gjerne kontakt. Vet du om noe svakheter med værstasjonen nær deg, tips oss gjerne.
</p>
<p>
Hilsen,<br>
Dagrun, Trygve, Chris og Karsten
</p>

</div>
</div>
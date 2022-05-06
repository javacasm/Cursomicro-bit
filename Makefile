microbit:
	pandoc --pdf-engine=xelatex   \
		-V papersize:a4paper    \
		--template=./LaTeX_ES.latex    \
		--reference-doc=plantilla_microbit.docx \
		-o  "Iniciación a la robótica con micro:bit.docx"  \
		Cabecera.md        \
		Cabecera_latex.md \
		1.0.Introduccion.md \
		"1.1.¿Porqué usar micro:bit?.md" \
		1.5.Trabajando_en_clase.md \
		2.1.Ejemplos_microbit.md \
		2.1.Otros_ejemplos_microbit.md \
		2.8.EsperandoPulsaciones.md \
		2.9.multitarea.md \
		3.0.Robots_microbit.md \
		3.1.0.MaQueen.md \
		3.1.2.Maqueen_3d.md \
		3.3.microbit_car.md \
		4.0.Complementos_microbit.md \
		5.0.Radio.md \
		5.2.ControlRemotoMaqueen.md \
		5.3.MandoIR.md \
		5.4.Coreografias.md \
		6.recursos.md

